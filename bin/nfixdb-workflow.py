#!/usr/bin/env python

import argparse
import time
from pathlib import Path


from nfixdb import nfdb_hmm
from nfixdb import nfdb_check
from nfixdb import nfdb_taxonomy
from nfixdb import nfdb_tophits
from nfixdb import nfdb_analysis
from nfixdb import nfdb_analysis_fasta
from nfixdb import nfdb_nitrogenase_fastas
from nfixdb import nfdb_ssu
from nfixdb import nfdb_final


def main():
	# Placeholder for main workflow logic
	parser = argparse.ArgumentParser()
	parser.add_argument("--seeds", required=True, help="Path to the folder containing the initial seed sequences")
	parser.add_argument("--gtdb", required=True, help="Path to the GTDB folder")
	parser.add_argument("--hmm-db", required=True, help="Path to Cerberus HMM database to use")
	parser.add_argument("--output", default="results-NFixDB", help="Path to output folder")
	parser.add_argument("--filter", action='store_true', help="Whether to filter sequences based on Cerberus results")
	parser.add_argument("--threads", type=int, default=1, help="Number of threads to use")

	args = parser.parse_args()

	seeds = Path(args.seeds)
	gtdb_proteins = Path(args.gtdb, "protein_faa_reps")
	gtdb_nucleotides = Path(args.gtdb, "protein_fna_reps")
	db_path = Path(args.hmm_db)
	output_folder = Path(args.output)
	threads = args.threads

	nitrogenase_fastas = output_folder/"fastas"
	nitrogenase_fastas.mkdir(parents=True, exist_ok=True)

	# Step 1: Check seed sequences with Cerberus
	print("Checking seed sequences with Cerberus...")
	start = time.time()
	filtered_seeds = nfdb_check.check_fastas_with_cerberus(seeds, db_path, output_folder/"cerberus_results"/"seeds", threads)
	if args.filter:
		print("Filtering seed sequences based on Cerberus results...")
		seeds = filtered_seeds
	end = time.time()
	print(f"Cerberus checking completed in {end - start:.2f} seconds.")

	# Step 2: Create HMMs from seed sequences
	output = output_folder/"alignments"
	hmm_db = list()
	if not output.exists():
		print("Creating HMMs from seed files...")
		start = time.time()
		for seed_file in Path(seeds).glob('*.faa'):
			hmm_db += [nfdb_hmm.create_hmm(seed_file, output, CPUs=threads)]
		end = time.time()
		print(f"Finished creating HMMs in {end - start:.2f} seconds")
	else:
		for hmm_file in output.glob('*.hmm'):
			hmm_db += [hmm_file]

	# Step 3: Scan GTDB proteins with created HMMs
	output = output_folder/"gtdb-results"
	if output.exists() is False:
		print("Scanning GTDB...")
		start = time.time()
		combined = output_folder/"combined.hmm"
		with open(combined, "w") as writer:
			for hmm in hmm_db:
				writer.write(open(hmm).read())
		nfdb_hmm.hmmscan(gtdb_proteins, output, combined, CPUs=threads)
		end = time.time()
		print(f"HMM scanning completed in {end - start:.2f} seconds.")

	# Step 4: Merge results with taxonomy
	print("Merging with GTDB and NCBI taxonomy")
	start = time.time()
	taxonomy_file = output_folder/"TSVs"/"evalue_taxonomy.tsv"
	nfdb_taxonomy.get_taxonomy(output_folder/"gtdb-results", taxonomy_file)
	end = time.time()
	print(f"Taxonomy merging completed in {end - start:.2f} seconds.")

	# Step 5: Filter for top hits
	print("Filtering for top hits...")
	start = time.time()
	top_hits_file = output_folder/"TSVs"
	nfdb_tophits.top_hits(taxonomy_file, top_hits_file)
	end = time.time()
	print(f"Top hits filtering completed in {end - start:.2f} seconds.")

	# Step 6: Analyze hits and fasta sequences
	print("Analyzing hits...")
	start = time.time()
	filtered_hits_file = output_folder/"TSVs"/"filteredhits.tsv"
	nfdb_analysis.analyze_hits(top_hits_file/"tophits.tsv", filtered_hits_file)
	end = time.time()
	print(f"Hit analysis completed in {end - start:.2f} seconds.")

	# Step 7: Analyze fasta sequences
	print("Analyzing fasta...")
	start = time.time()
	filtered_fasta_file = output_folder/"TSVs"/"filteredfasta.tsv"
	nfdb_analysis_fasta.analyze_fasta(top_hits_file/"topfasta.tsv", filtered_fasta_file)
	end = time.time()
	print(f"Fasta analysis completed in {end - start:.2f} seconds.")

	# Step 8: Extract nitrogenase sequences
	print("Extracting nitrogenase sequences...")
	start = time.time()
	nfdb_nitrogenase_fastas.extract_fastas(filtered_fasta_file, output_folder/"fastas", gtdb_proteins)
	end = time.time()
	print(f"Nitrogenase sequence extraction completed in {end - start:.2f} seconds.")

	# Step 9: Check nitrogenase sequences with Cerberus
	print("Checking nitrogenase sequences with Cerberus...")
	start = time.time()
	filtered_fastas = nfdb_check.check_fastas_with_cerberus(nitrogenase_fastas, db_path, output_folder/"cerberus_results"/"fastas", 12)
	if args.filter:
		print("Filtering nitrogenase sequences based on Cerberus results...")
		nitrogenase_fastas = filtered_fastas
	end = time.time()
	print(f"Cerberus checking completed in {end - start:.2f} seconds.")

	# Step 10: Create HMMs from nitrogenase sequences
	print("Creating HMMs from nitrogenase sequences...")
	start = time.time()
	nitro_hmm_db = list()
	output = output_folder/"nitro-alignments"
	for seed_file in Path(nitrogenase_fastas).glob('*.faa'):
		nitro_hmm_db += [nfdb_hmm.create_hmm(seed_file, output, CPUs=threads)]
	end = time.time()
	print(f"Finished creating nitrogenase HMMs in {end - start:.2f} seconds")

	# Step 11: Generate SSU sequences
	print("Generating SSU sequences...")
	start = time.time()
	ssu_path = output_folder/"SSUs"
	nfdb_ssu.generate_ssu(filtered_hits_file, ssu_path, gtdb_nucleotides, threads=threads)
	end = time.time()
	print(f"SSU generation completed in {end - start:.2f} seconds.")

	# Step 12: Add SSU sequences to filtered hits
	print("Adding SSU sequences to filtered hits...")
	start = time.time()
	filtered_hits_ssu_file = output_folder / "TSVs" / "filteredhits_SSU.tsv"
	nfdb_ssu.add_ssu_to_filteredhits(filtered_hits_file, ssu_path, filtered_hits_ssu_file)
	end = time.time()
	print(f"SSU addition completed in {end - start:.2f} seconds.")

	# Step 13: Finalize NFixDB
	print("Finalizing NFixDB sql and tsv files...")
	start = time.time()
	final_tsv = output_folder / "NFixDB.tsv"
	nfdb_final.finalize_database(output_folder/"TSVs", final_tsv, output_folder/"NFixDB.sql")
	end = time.time()
	print(f"NFixDB finalization completed in {end - start:.2f} seconds.")

	return 0


if __name__ == "__main__":
	exit(main())

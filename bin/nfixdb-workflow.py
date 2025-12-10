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
	parser.add_argument("--output", default="results-NFixDB", help="Path to output folder")
	parser.add_argument("--threads", type=int, default=1, help="Number of threads to use")

	args = parser.parse_args()

	gtdb_proteins = Path(args.gtdb, "protein_faa_reps")
	gtdb_nucleotides = Path(args.gtdb, "protein_fna_reps")
	output_folder = Path(args.output)
	threads = args.threads

	output = output_folder/"alignments"
	hmm_db = list()
	if not output.exists():
		print("Creating HMMs from seed files...")
		start = time.time()
		for seed_file in Path(args.seeds).glob('*.faa'):
			hmm_db += [nfdb_hmm.create_hmm(seed_file, output, CPUs=threads)]
		end = time.time()
		print(f"Finished creating HMMs in {end - start:.2f} seconds")
	else:
		for hmm_file in output.glob('*.hmm'):
			hmm_db += [hmm_file]

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

	print("Merging with GTDB and NCBI taxonomy")
	start = time.time()
	taxonomy_file = output_folder/"TSVs"/"evalue_taxonomy.tsv"
	nfdb_taxonomy.get_taxonomy(output_folder/"gtdb-results", taxonomy_file)
	end = time.time()
	print(f"Taxonomy merging completed in {end - start:.2f} seconds.")

	print("Filtering for top hits...")
	start = time.time()
	top_hits_file = output_folder/"TSVs"
	nfdb_tophits.top_hits(taxonomy_file, top_hits_file)
	end = time.time()
	print(f"Top hits filtering completed in {end - start:.2f} seconds.")

	print("Analyzing hits...")
	start = time.time()
	filtered_hits_file = output_folder/"TSVs"/"filteredhits.tsv"
	nfdb_analysis.analyze_hits(top_hits_file/"tophits.tsv", filtered_hits_file)
	end = time.time()
	print(f"Hit analysis completed in {end - start:.2f} seconds.")

	print("Analyzing fasta...")
	start = time.time()
	filtered_fasta_file = output_folder/"TSVs"/"filteredfasta.tsv"
	nfdb_analysis_fasta.analyze_fasta(top_hits_file/"topfasta.tsv", filtered_fasta_file)
	end = time.time()
	print(f"Fasta analysis completed in {end - start:.2f} seconds.")

	print("Extracting nitrogenase sequences...")
	start = time.time()
	nfdb_nitrogenase_fastas.extract_fastas(filtered_fasta_file, output_folder/"fastas", gtdb_proteins)
	end = time.time()
	print(f"Nitrogenase sequence extraction completed in {end - start:.2f} seconds.")

	print("Checking nitrogenase sequences with Cerberus...")
	start = time.time()
	nfdb_check.check_fastas_with_cerberus(output_folder/"fastas", Path("/home/jlfiguer/database/db-metacerberus/"), output_folder/"cerberus_results")
	end = time.time()
	print(f"Cerberus checking completed in {end - start:.2f} seconds.")

	return 0

	print("Generating SSU sequences...")
	start = time.time()
	ssu_path = output_folder/"SSUs"
	nfdb_ssu.generate_ssu(filtered_hits_file, ssu_path, gtdb_nucleotides, threads=threads)
	end = time.time()
	print(f"SSU generation completed in {end - start:.2f} seconds.")

	print("Adding SSU sequences to filtered hits...")
	start = time.time()
	filtered_hits_ssu_file = output_folder / "TSVs" / "filteredhits_SSU.tsv"
	nfdb_ssu.add_ssu_to_filteredhits(filtered_hits_file, ssu_path, filtered_hits_ssu_file)
	end = time.time()
	print(f"SSU addition completed in {end - start:.2f} seconds.")

	print("Finalizing NFixDB...")
	start = time.time()
	final_tsv = output_folder / "NFixDB.tsv"
	nfdb_final.finalize_database(output_folder/"TSVs", final_tsv, output_folder/"NFixDB.sql")
	end = time.time()
	print(f"NFixDB finalization completed in {end - start:.2f} seconds.")

	return 0


if __name__ == "__main__":
	exit(main())

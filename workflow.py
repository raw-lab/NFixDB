#!/usr/bin/env python

import argparse
import time
from pathlib import Path

import lib.nfdb_hmm as nfdb_hmm
import lib.nfdb_taxonomy as nfdb_taxonomy
import lib.nfdb_tophits as nfdb_tophits
import lib.nfdb_analysis as nfdb_analysis
import lib.nfdb_analysis_fasta as nfdb_analysis_fasta
import lib.nfdb_nitrogenase_fastas as nfdb_nitrogenase_fastas
import lib.nfdb_ssu as nfdb_ssu
import lib.nfdb_final as nfdb_final


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
	if not output.exists():
		print("Creating HMMs from seed files...")
		hmm_db = list()
		start = time.time()
		for seed_file in Path(args.seeds).glob('*.faa'):
			hmm_db += [nfdb_hmm.create_hmm(seed_file, output, CPUs=threads)]
		end = time.time()
		print(f"Finished creating HMMs in {end - start:.2f} seconds")

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

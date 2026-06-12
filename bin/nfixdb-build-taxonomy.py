#!/usr/bin/env python

import gzip
from pathlib import Path
import urllib.request


NCBI_URL = Path("data.gtdb.aau.ecogenomic.org/releases/latest/")
OUTFILE = Path("complete_taxonomy.tsv")




def main():
	"""
	Download and build taxonomy lookup table
	"""

	print("Downloading files...")
	for filename in ["ar53_taxonomy.tsv", 	"ar53_metadata.tsv.gz", "bac120_taxonomy.tsv", "bac120_metadata.tsv.gz"]:
		urllib.request.urlretrieve(f"https://{NCBI_URL/filename}", filename)

	gtdb = dict()
	ncbi = dict()

	print("Reading GTDB taxonomy data...")
	for filename in ["ar53_taxonomy.tsv", "bac120_taxonomy.tsv"]:
		with open(filename) as reader:
			for line in reader:
				line = line.split()
				gtdb[line[0]] = line[1]
	print("Reading NCBI metadata")
	for filename in ["ar53_metadata.tsv.gz", "bac120_metadata.tsv.gz"]:
		with gzip.open(filename, 'rt') as reader:
			reader.readline()
			for line in reader:
				line = line.split()
				ncbi[line[0]] = [line[20], line[81], line[83]]

	print("Saving final tsv file...")
	with OUTFILE.open('w') as writer:
		print("GenomeID", "GTDB_Tax", "NCBI_TaxID", "NCBI_Tax", sep="\t", file=writer)
		for k,v in ncbi.items():
			print(k, v[0], v[1], v[2], sep="\t", file=writer)

	return 0

if __name__ == "__main__":
	main()

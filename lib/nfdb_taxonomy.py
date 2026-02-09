#!/usr/bin/python3

"""taxonomy.py
Loads the taxonomy file and creates a table with matches from hmmsearch.
"""

import gzip
from pathlib import Path
import re
import pkg_resources as pkg

#TAXONOMY = pkg.resource_filename("nfixdb", "data")
TAXONOMY = Path("data", "TSVs")


def get_taxonomy(hitpath, outfile):
	# Get taxonomy from GTDB and NCBI
	outfile = Path(outfile)
	if outfile.exists():
		print("Merged taxonomy file already exists:", outfile)
		return outfile

	taxonomy = Path(TAXONOMY, "complete_taxonomy.tsv.gz")
	tax_db = dict()
	with gzip.open(taxonomy, "rt") as reader:
		line = reader.readline()
		for line in reader:
			line = line.rstrip('\r\n').split('\t')
			tax_db[line[0]] = line[1:]

	#complete_df = pd.read_csv(taxonomy, sep='\t')

	# regex patterns
	reGenomeID = re.compile(r'^([\w]+_[\w]+.[\w])')
	#reGeneName = re.compile(r'([a-zA-Z]+)-([a-zA-Z]+)')
	reGeneName = re.compile(r'([a-zA-Z]+)')
	reDescription = re.compile(r'# ([0-9]+) # ([0-9]+)')

# https://ftp.ncbi.nih.gov/pub/taxonomy/
# datasets summary genome accession GCA_026014805.1


	# Parse through files in output directory from hmmsearch
	outfile.parent.mkdir(parents=True, exist_ok=True)
	oor_file = outfile.with_name("oor_taxonomy.tsv")
	with outfile.open("w") as writer, oor_file.open("w") as oor_writer, open("log-taxonomy.txt", "w") as log_writer:
		# Write headers
		print("GenomeID", "GeneName", "SeqID", "EValue", "Bitscore", "Location", "AlnLength", "SeqLength", "GTDB_Tax", "NCBI_TaxID", "NCBI_Tax", sep='\t', file=writer)
		print("GenomeID", "GeneName", "SeqID", "EValue", "Bitscore", "Location", "AlnLength", "SeqLength", "GTDB_Tax", "NCBI_TaxID", "NCBI_Tax", sep='\t', file=oor_writer)
		for filename in Path(hitpath).glob("*"):
			# RegEx for the GenomeID
			match = reGenomeID.match(filename.stem)
			if match:
				genomeID = match.group()
			else:
				print(f"Could not parse GenomeID from filename {filename}")
				continue

			tax = tax_db.get(genomeID, None)
			if tax is None:
				print(f"Could not find taxonomy for GenomeID {genomeID}", file=log_writer)
				continue

			#path = Path(hitpath, filename)
			with filename.open() as reader:
				for line in reader:
					line = line.rstrip().split('\t')
					gene_name = reGeneName.match(line[0]).group(1)
					hit_id = line[1]
					evalue = float(line[2])
					bitscore = float(line[3])
					match = reDescription.match(line[5])
					if match:
						location = match.group(1) + "-" + match.group(2)
					else:
						location = "N/A"
					alength = int(line[4])
					slength = int(match.group(2)) - int(match.group(1))
					# Check the evalue cutoff and append the data to the corresponding lists
					if evalue < 9.9e-10:
						print(genomeID, gene_name, hit_id, evalue, bitscore, location, alength, slength, *tax, sep='\t', file=writer)
					# If it does not meet the evalue cutoff, append it to the OOR lists
					else:
						print(genomeID, gene_name, hit_id, evalue, bitscore, location, alength, slength, *tax, sep='\t', file=oor_writer)

			continue

	return outfile

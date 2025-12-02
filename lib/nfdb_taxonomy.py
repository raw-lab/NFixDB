#!/usr/bin/python3

"""taxonomy.py
Loads the taxonomy file and creates a table with matches from hmmsearch.
"""

import gzip
from pathlib import Path
import re
import argparse
import pandas as pd
from Bio import SearchIO

#import pkg_resources as pkg
#TAXONOMY = pkg.resource_filename("NFixDB", "data")
TAXONOMY = Path("data", "TSVs")


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--taxonomy', type=str, default='data/TSVs/complete_taxonomy.tsv', help="Path to the taxonomy file")
parser.add_argument('--hitpath', type=str, default='results/bac120_ar53/', help="Path to the folder containing the HMM hits")
parser.add_argument('-o', '--outfile', type=str, default='results/TSVs/evalue_taxonomy.tsv', help="Path to the folder containing the HMM hits")

#args = parser.parse_args()

def get_taxonomy(hitpath, outfile):
	# Get taxonomy from GTDB and NCBI
	outfile = Path(outfile)

	taxonomy = Path(TAXONOMY, "complete_taxonomy.tsv.gz")
	tax_db = dict()
	with gzip.open(taxonomy, "rt") as reader:
		line = reader.readline()
		for line in reader:
			line = line.rstrip('\r\n').split('\t')
			tax_db[line[0]] = line[1:]

	#complete_df = pd.read_csv(taxonomy, sep='\t')

	# Create empty lists
	result_target = []
	query_id = []
	hit_id = []
	evalue = []
	bitscore = []
	location = []
	alength = []
	slength = []

	#OOR stands for "Out Of Range", AKA the values that do not meet our E-value threshold
	oor_target = []
	oor_queryid = []
	oor_hitid = []
	oor_evalue = []
	oor_bitscore = []
	oor_location = []
	oor_alength = []
	oor_slength = []

	# regex patterns
	reGenomeID = re.compile(r'^([\w]+_[\w]+.[\w])')
	#reGeneName = re.compile(r'([a-zA-Z]+)-([a-zA-Z]+)')
	reGeneName = re.compile(r'([a-zA-Z]+)')
	reDescription = re.compile(r'# ([0-9]+) # ([0-9]+)')

	#Taxonomy:
	#GenomeID	GTDB_Tax	NCBI_TaxID	NCBI_Tax
	#GB_GCA_003158115.1	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.

	#Hit file name
	#GB_GCA_003158115.1_protein-combined.tsv

	#Contents of hit file
	#h.name, query_name, evalue, score, length, align.target_from, align.target_to,
	#PMGM01000076.1_11       nflH_121623     2.8E-120        397.6   263     5       261
	#PMGM01000034.1_5        nflH_121623     1.1E-114        379.1   276     2       270

	#OUTPUT:
	#GenomeID	GeneName	SeqID	EValue	Bitscore	Location	AlnLength	SeqLength	GTDB_Tax	NCBI_TaxID	NCBI_Tax
	#GB_GCA_003158115.1	anfD	PMGM01000034.1_8	0.0	1093.7	4051-5613	516	1562	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164.0	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.
	#GB_GCA_003158115.1	anfD	PMGM01000034.1_8	0.0	1093.7	1-516	521	521	521



#GB_GCA_003158115.1	vnfD	PMGM01000034.1_8	5.2e-210	695.1	4051-5613	463	1562	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164.0	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.
#GB_GCA_003158115.1	vnfD	PMGM01000048.1_28	3.1e-026	89.1	27273-28805	375	1532	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164.0	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.
#GB_GCA_003158115.1	vnfD	PMGM01000048.1_29	5.7e-016	55.2	28802-30160	275	1358	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164.0	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.
#GB_GCA_003158115.1	vnfD	PMGM01000034.1_10	2.4e-012	43.3	5989-7377	190	1388	d__Archaea;p__Methanobacteriota;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium_B;s__Methanobacterium_B sp003158115	2164.0	d__Archaea;p__Euryarchaeota;x__Methanomada group;c__Methanobacteria;o__Methanobacteriales;f__Methanobacteriaceae;g__Methanobacterium;x__unclassified Methanobacterium;s__Methanobacterium sp.


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
			for result in SearchIO.parse(str(path), 'hmmer3-text'):
				for item in result.hits:
					# RegEx for the gene name
					gene_name = reGeneName.match(result.id).group(1)
					# Check the evalue cutoff and append the data to the corresponding lists
					if item.evalue < 9.9e-10:
						result_target += [genomeID]
						query_id += [gene_name]
						hit_id += [item.id]
						evalue += [item.evalue]
						bitscore += [item.bitscore]
						match = reDescription.match(item.description)
						location += [match.group(1) + "-" + match.group(2)]
						alength += [item.hsps[0].aln_span]
						slength += [int(match.group(2))-int(match.group(1))]
					# If it does not meet the evalue cutoff, append it to the OOR lists
					else:
						oor_target += [genomeID]
						oor_queryid += [gene_name]
						oor_hitid += [item.id]
						oor_evalue += [item.evalue]
						oor_bitscore += [item.bitscore]
						match = reDescription.match(item.description)
						oor_location += [match.group(1) + "-" + match.group(2)]
						oor_alength += [item.hsps[0].aln_span]
						oor_slength += [int(match.group(2))-int(match.group(1))]

	return outfile

	# Convert the good stuff to a TSV
	evalue_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 
					'Location' : location, 'AlnLength' : alength, 'SeqLength' : slength}
	evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')
	evalue_df = pd.merge(evalue_df, complete_df, on = "GenomeID", how = "left").drop_duplicates()
	outfile = Path(outfile)
	outfile.parent.mkdir(parents=True, exist_ok=True)
	evalue_df.to_csv(outfile, sep = "\t", index=False)

	# Convert the bad stuff to a TSV
	oor_dict = {'GenomeID' : oor_target, 'GeneName' : oor_queryid, 'SeqID' : oor_hitid, 'EValue' : oor_evalue, 'Bitscore' : oor_bitscore, 
				'Location' : oor_location, 'AlnLength' : oor_alength, 'SeqLength' : oor_slength}
	oor_df = pd.DataFrame(oor_dict).sort_values('EValue')
	oor_df = pd.merge(oor_df, complete_df, on = "GenomeID", how = "left").drop_duplicates()
	oor_file = outfile.with_name("oor_taxonomy.tsv")
	oor_df.to_csv(oor_file, sep = "\t", index=False)

	return outfile

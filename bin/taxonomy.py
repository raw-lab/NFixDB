#!/usr/bin/python3

"""taxonomy.py
Loads the taxonomy file and creates a table with matches from hmmsearch.
"""

import os
from pathlib import Path
import re
import argparse
import pandas as pd
from Bio import SearchIO


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--taxonomy', type=str, default='data/TSVs/complete_taxonomy.tsv', help="Path to the taxonomy file")
parser.add_argument('--hitpath', type=str, default='results/bac120_ar53/', help="Path to the folder containing the HMM hits")
parser.add_argument('-o', '--outfile', type=str, default='results/TSVs/evalue_taxonomy.tsv', help="Path to the folder containing the HMM hits")

args = parser.parse_args()

# Get taxonomy from GTDB and NCBI
complete_df = pd.read_csv(args.taxonomy, sep='\t')

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
reGeneName = re.compile(r'([a-zA-Z]+)-([a-zA-Z]+)')
reDescription = re.compile(r'# ([0-9]+) # ([0-9]+)')

# Parse through files in output directory from hmmsearch
directory = args.hitpath
for filename in os.listdir(directory):
    # RegEx for the GenomeID
    match = reGenomeID.match(filename)
    if match:
        genomeID = match.group()
    else:
        continue

    path = Path(directory, filename)
    if path.is_file():
        # Parse file using SearchIO/HmmerIO
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

# Convert the good stuff to a TSV
evalue_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 
                'Location' : location, 'AlnLength' : alength, 'SeqLength' : slength}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')
evalue_df = pd.merge(evalue_df, complete_df, on = "GenomeID", how = "left").drop_duplicates()
outfile = Path(args.outfile)
outfile.parent.mkdir(parents=True, exist_ok=True)
evalue_df.to_csv(outfile, sep = "\t", index=False)

# Convert the bad stuff to a TSV
oor_dict = {'GenomeID' : oor_target, 'GeneName' : oor_queryid, 'SeqID' : oor_hitid, 'EValue' : oor_evalue, 'Bitscore' : oor_bitscore, 
            'Location' : oor_location, 'AlnLength' : oor_alength, 'SeqLength' : oor_slength}
oor_df = pd.DataFrame(oor_dict).sort_values('EValue')
oor_df = pd.merge(oor_df, complete_df, on = "GenomeID", how = "left").drop_duplicates()
outfile = outfile.with_name("oor_taxonomy.tsv")
oor_df.to_csv(outfile, sep = "\t", index=False)

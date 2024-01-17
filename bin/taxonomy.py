#!/usr/bin/python3

import pandas as pd
from Bio import SearchIO
import os
import re

# Get taxonomy from GTDB
complete_df = pd.DataFrame(pd.read_table('TSVs/complete_taxonomy.tsv'))

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

# Parse through files in output directory
directory = 'bac120_ar53_results_i2-1' 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # RegEx fo the GenomeID
    reg = r'^([\w]+_[\w]+.[\w])'
    regex = re.match(reg, filename).group()
    if os.path.isfile(f):
        # Parse file using SearchIO/HmmerIO
        for result in SearchIO.parse(f, 'hmmer3-text'):
            for item in result.hits:
                # RegEx for the gene name
                reg2 = r'([a-zA-Z]+)-([a-zA-Z]+)'
                regex2 = re.match(reg2, result.id).group(1)
                # Check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10:
                    result_target.append(regex)
                    query_id.append(regex2)
                    hit_id.append(item.id)
                    evalue.append(item.evalue)
                    bitscore.append(item.bitscore)
                    reg3 = r'# ([0-9]+) # ([0-9]+)'
                    location.append(re.match(reg3, item.description).group(1) + "-" + re.match(reg3, item.description).group(2))
                    alength.append(item.hsps[0].aln_span)
                    slength.append(int(re.match(reg3, item.description).group(2))-int(re.match(reg3, item.description).group(1)))
                # If it does not meet the evalue cutoff, append it to the OOR lists
                else:
                    oor_target.append(regex)
                    oor_queryid.append(regex2)
                    oor_hitid.append(item.id)
                    oor_evalue.append(item.evalue)
                    oor_bitscore.append(item.bitscore)
                    oreg3 = r'# ([0-9]+) # ([0-9]+)'
                    oor_location.append(re.match(oreg3, item.description).group(1) + "-" + re.match(oreg3, item.description).group(2))
                    oor_alength.append(item.hsps[0].aln_span)
                    oor_slength.append(int(re.match(oreg3, item.description).group(2))-int(re.match(oreg3, item.description).group(1)))

# Convert the good stuff to a TSV
evalue_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 
                'Location' : location, 'AlnLength' : alength, 'SeqLength' : slength}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')
evalue_df = pd.merge(evalue_df, complete_df, on = "GenomeID", how = "left").drop(columns = ["Unnamed: 0"]).drop_duplicates()

evalue_df.to_csv("TSVs/evalue_taxonomy.tsv", sep = "\t")

# Convert the bad stuff to a TSV
oor_dict = {'GenomeID' : oor_target, 'GeneName' : oor_queryid, 'SeqID' : oor_hitid, 'EValue' : oor_evalue, 'Bitscore' : oor_bitscore, 
            'Location' : oor_location, 'AlnLength' : oor_alength, 'SeqLength' : oor_slength}
oor_df = pd.DataFrame(oor_dict).sort_values('EValue')
oor_df = pd.merge(oor_df, complete_df, on = "GenomeID", how = "left").drop(columns = ["Unnamed: 0"]).drop_duplicates()

oor_df.to_csv("TSVs/oor_taxonomy.tsv", sep = "\t")



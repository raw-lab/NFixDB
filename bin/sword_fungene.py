#!/usr/bin/env/python3

import pandas as pd
import os
import re

# Set directory, empty list of dataframes for each output file, and empty lists for query/subject seqeunces
directory = 'sword/FunGene'
dfs = []
nSeq = []
bSeq = []

# Populate dataframe list with each file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # RegEx for NFixDBSeq
    reg = r'([^-]*)'
    regex = re.match(reg, filename).group(1)
    
    # RegEx for FunGeneSeq
    reg2 = r'\_(.*?)\_'
    regex2 = re.search(reg2, filename).group(1)

    # Read each output file, ignoring the comment lines and add it to the dfs list
    df = pd.read_table(f, index_col=None, header=0, comment='#')
    dfs.append(df)
    
    # Add query and subject sequences to their corresponding lists
    for line in df.iterrows():
        nSeq.append(regex)
        bSeq.append(regex2)

# Combine all dataframes into one large dataframe
fungene_comb = pd.concat(dfs, axis=0, ignore_index=True)

# Add in the query and subject sequences
fungene_comb.insert(1, 'FunGeneSeq', bSeq)
fungene_comb.insert(3, 'NFixDBSeq', nSeq)

# Make everything look a little better
fungene_comb = fungene_comb.drop_duplicates().drop(index=[10, 350, 690, 1030])
fungene_comb = fungene_comb.rename(columns={'Query id': 'FunGeneID', 'Subject id': 'NFixDBID', '% identity': '%Identity', 
                    'alignment length': 'AlnLength', 'mismatches': 'Mismatches', 'gap openings': 'GapOpens', 'q. start': 'QueryStart', 
                    'q. end': 'QueryEnd', 's. start': 'SeqStart', 's. end': 'SeqEnd', 'e-value': 'EValue', 'score': 'Score'})

# Convert to TSV
fungene_comb.to_csv("TSVs/fungene_sword.tsv", sep = "\t")


# Convert columns to number datatypes and get full length alignments (≤ 220 AA)
fungene_comb = fungene_comb.astype({'AlnLength': 'int', 'EValue': 'float', 'Score': 'int'})
fungene_df = fungene_comb[fungene_comb.AlnLength >= 220]

# Get the highest result for each sequence ID
fungene_df = fungene_df.sort_values('EValue')
fungene_df = fungene_df.groupby(["FunGeneID"]).first()

# Convert to TSV
fungene_df.to_csv("TSVs/fungene_sword_hits.tsv", sep = "\t")

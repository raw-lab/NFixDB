#!/usr/bin/env/python3

import pandas as pd
import os
import re

# Set directory, empty list of dataframes for each output file, and empty lists for query/subject seqeunces
directory = 'sword/i2/Zehr'
dfs = []
nSeq = []
bSeq = []

# Populate dataframe list with each file
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # RegEx for NFixDBSeq
    reg = r'([^-]*)'
    regex = re.match(reg, filename).group(1)
    
    # RegEx for zehrSeq
    reg2 = r'\_(.*?)\_'
    regex2 = re.search(reg2, filename).group(1)

    # Read each output file, ignoring the comment lines and add it to the dfs list
    df = pd.read_table(f, index_col=None, header=0, comment='#')
    dfs.append(df)
    
    # Add query and subject sequences to their corresponding lists
    for line in df.iterrows():
        nSeq.append(regex)
        bSeq.append(regex2)
    
    print(f + " done")

# Combine all dataframes into one large dataframe
zehr_comb = pd.concat(dfs, axis=0, ignore_index=True)

# Add in the query and subject sequences
zehr_comb.insert(1, 'ZehrSeq', bSeq)
zehr_comb.insert(3, 'NFixDBSeq', nSeq)

# Make everything look a little better
zehr_comb = zehr_comb.drop_duplicates()
zehr_comb = zehr_comb[zehr_comb['Query id'] != 'Query id']
zehr_comb = zehr_comb.rename(columns={'Query id': 'ZehrID', 'Subject id': 'NFixDBID', '% identity': 'PercIdentity', 
                    'alignment length': 'AlnLength', 'mismatches': 'Mismatches', 'gap openings': 'GapOpens', 'q. start': 'QueryStart', 
                    'q. end': 'QueryEnd', 's. start': 'SeqStart', 's. end': 'SeqEnd', 'e-value': 'EValue', 'score': 'Score'})

# Convert to TSV
zehr_comb.to_csv("TSVs/zehr_sword.tsv", sep = "\t")


# Convert columns to number datatypes and get full length alignments (≤ 220 AA)
zehr_comb = zehr_comb.astype({'AlnLength': 'int', 'PercIdentity': 'int', 'EValue': 'float', 'Score': 'int'})
zehr_df = zehr_comb[zehr_comb.AlnLength >= 220]
zehr_df = zehr_df[zehr_df.PercIdentity >= 50] 
zehr_df = zehr_df[zehr_df.EValue <= 9.9e-10]

# Get the highest result for each sequence ID
zehr_df = zehr_df.sort_values('EValue')
zehr_df = zehr_df.groupby(["ZehrID"]).first()

# Convert to TSV
zehr_df.to_csv("TSVs/zehr_sword_hits.tsv", sep = "\t")

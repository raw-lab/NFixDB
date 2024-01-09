#!/usr/bin/python3

import pandas as pd

# Get evalue_taxonomy TSV
df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i2-3.tsv'))

# Take subset of dataframe
top_fasta = pd.DataFrame(columns=['GenomeID', 
    'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
    'nifD', 'EV_nifD', 'bitscore_nifD', 'location_nifD', 'alnLen_nifD', 'seqLen_nifD',
    'nifK', 'EV_nifK', 'bitscore_nifK', 'location_nifK', 'alnLen_nifK', 'seqLen_nifK',
    'anfH', 'EV_anfH', 'bitscore_anfH', 'location_anfH', 'alnLen_anfH', 'seqLen_anfH',
    'anfD', 'EV_anfD', 'bitscore_anfD', 'location_anfD', 'alnLen_anfD', 'seqLen_anfD',
    'anfK', 'EV_anfK', 'bitscore_anfK', 'location_anfK', 'alnLen_anfK', 'seqLen_anfK',
    'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'location_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
    'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'location_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
    'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'location_vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
    'nflH', 'EV_nflH', 'bitscore_nflH', 'location_nflH', 'alnLen_nflH', 'seqLen_nflH',
    'nflD', 'EV_nflD', 'bitscore_nflD', 'location_nflD', 'alnLen_nflD', 'seqLen_nflD',
    'ChlB', 'EV_ChlB', 'bitscore_ChlB', 'location_ChlB', 'alnLen_ChlB', 'seqLen_ChlB',
    'ChIl', 'EV_ChIl', 'bitscore_ChIl', 'location_ChIl', 'alnLen_ChIl', 'seqLen_ChIl',
    'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'location_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',])

# First sort to find top result for sequence ID (temporary file later deleted)
df2 = df.groupby(["GenomeID", "SeqID"]).first()
df2 = df2.sort_values("EValue").drop(columns="Unnamed: 0")
df2.to_csv("fasta_temp.tsv", sep = "\t")

# Second sort to find top result for sequence ID and gene (temporary file later deleted)
df3 = pd.DataFrame(pd.read_table('fasta_temp.tsv'))
df3 = df3.groupby(["GenomeID", "GeneName"]).first()
df3.to_csv("fasta_temp2.tsv", sep = "\t")
df3 = pd.DataFrame(pd.read_table('fasta_temp2.tsv'))

# Loop through top hits dataframe to put it in the dictionary in the corressponding columns
for index, row in df3.iterrows():
    top_fasta['GenomeID'] = df3['GenomeID']
    for col in top_fasta.columns:
        if row['GeneName'] == col:
            if row['EValue'] < 9.9e-15 or row['Bitscore'] > 50 or row['AlnLength'] > 125:
                ev = "EV_" + col
                bs = "bitscore_" + col
                lo = "location_" + col
                al = "alnLen_" + col
                sl = "seqLen_" + col
                top_fasta.loc[top_fasta.GenomeID == row['GenomeID'], [col, ev, bs, lo, al, sl]] = row['SeqID'], row['EValue'], row['Bitscore'], row['Location'], row['AlnLength'], row['SeqLength']

# Drop duplicates and make a TSV
top_fasta = top_fasta.drop_duplicates().dropna(thresh=7)
top_fasta.to_csv("TSVs/topfasta_i2-3.tsv", sep = "\t")



#!/usr/bin/python3

"""tophits.py
Reads the combined taxonomy/hits file and filters for the top hits.
"""

import argparse
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='results/i1/TSVs/evalue_taxonomy.tsv', help="Path to the evalue_taxonomy file")
parser.add_argument('-o', '--outpath', type=str, default='results/i1/TSVs', help="Path to the folder containing the HMM hits")

args = parser.parse_args()

outpath = Path(args.outpath)

# Get evalue_taxonomy TSV
df = pd.DataFrame(pd.read_table(args.input))

# Take subset of dataframe
topHits_df = pd.DataFrame(columns=[
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
    'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'location_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',
    'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax'])

top_fasta = pd.DataFrame(columns=[
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
df = df.groupby(["GenomeID", "SeqID"]).first()
df = df.sort_values("EValue")
df.to_csv("temp_hits.tsv", sep = "\t")

# Second sort to find top result for sequence ID and gene (temporary file later deleted)
df = pd.DataFrame(pd.read_table('temp_hits.tsv'))
df = df.groupby(["GenomeID", "GeneName"]).first()
df.to_csv("temp_hits.tsv", sep = "\t")
df = pd.DataFrame(pd.read_table('temp_hits.tsv'))

Path('temp_hits.tsv').unlink()

# Loop through top hits dataframe to put it in the corressponding columns
for index, row in df.iterrows():
    col = row['GeneName']
    ev = "EV_" + col
    bs = "bitscore_" + col
    lo = "location_" + col
    al = "alnLen_" + col
    sl = "seqLen_" + col
    topHits_df.at[row['GenomeID'], [col, ev, bs, lo, al, sl, 'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax']] = row['SeqID'], row['EValue'], row['Bitscore'], row['Location'], row['AlnLength'], row['SeqLength'], row['GTDB_Tax'], row['NCBI_TaxID'], row['NCBI_Tax']

    if row['EValue'] < 9.9e-15 or row['Bitscore'] > 50 or row['AlnLength'] > 125:
        top_fasta.at[row['GenomeID'], [col, ev, bs, lo, al, sl]] = row['SeqID'], row['EValue'], row['Bitscore'], row['Location'], row['AlnLength'], row['SeqLength']

# Drop duplicates and make a TSV
topHits_df = topHits_df.drop_duplicates()
topHits_df.to_csv(outpath/"tophits.tsv", sep = "\t", index=True, index_label="GenomeID")

top_fasta = top_fasta.drop_duplicates().dropna(thresh=7)
top_fasta.to_csv(outpath/"topfasta.tsv", sep = "\t", index=True, index_label="GenomeID")

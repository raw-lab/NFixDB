#!/usr/bin/python3

import os
import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='results/i1/TSVs/filteredhits.tsv', help="Path to the filteredhits.tsv file")
parser.add_argument('-o', '--output', type=str, default='results/i1/TSVs/filteredhits_SSU.tsv', help="Path to the output file filteredhits_SSU.tsv")
parser.add_argument('-s', '--ssu', type=str, default='results/i1/SSUs', help="Path to the output folder containing Barnap results")

args = parser.parse_args()


# Get filteredhits TSV
df = pd.DataFrame(pd.read_table(args.input))

# Create empty lists for each SSU
s5 = []
s58 = []
s16 = []
s23 = []

ssu = pd.DataFrame(columns=['GenomeID', '5S', '5.8S', '16S', '23S'])

# Populate SSU dataframe with SSUs that correspond to the genome ID
directory = args.ssu
for index, row in df.iterrows():
    ssu['GenomeID'] = df['GenomeID']
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        if os.path.isfile(f):
            base = os.path.splitext(file)[0]
            if base == row['GenomeID']:
                with open(f, 'r') as fi:
                    for line in fi:
                        if line.startswith(">"):
                            split = line.split("::")
                            if '5S' in split[0]:
                                s5.append(split[1].strip())
                            elif '5.8S' in split[0]:
                                s58.append(split[1].strip())
                            elif '16S' in split[0]:
                                s16.append(split[1].strip())
                            elif '23S' in split[0]:
                                s23.append(split[1].strip())
                ssu.loc[ssu['GenomeID']==row['GenomeID'], '5S'] = ', '.join(str(v) for v in s5)
                ssu.loc[ssu['GenomeID']==row['GenomeID'], '5.8S'] = ', '.join(str(v) for v in s58)
                ssu.loc[ssu['GenomeID']==row['GenomeID'], '16S'] = ', '.join(str(v) for v in s16)
                ssu.loc[ssu['GenomeID']==row['GenomeID'], '23S'] = ', '.join(str(v) for v in s23)
                s5.clear()
                s58.clear()
                s16.clear()
                s23.clear()

# Convert to TSV
final_df = pd.merge(df, ssu, on = "GenomeID", how="left")
final_df.to_csv(args.output, sep = "\t", index=False)

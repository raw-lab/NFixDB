#!/usr/bin/python3

import pandas as pd

df = pd.DataFrame(pd.read_table('TSVs/oDB_class.tsv'))

# Sort to find top result for sequence ID and E value
df2 = df.groupby(["SeqID"]).first()
df2 = df2.sort_values("EValue").drop(columns="Unnamed: 0").reset_index()

# Convert to TSV
df2.to_csv("TSVs/oDB_hits.tsv", sep = "\t")


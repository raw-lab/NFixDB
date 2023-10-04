import pandas as pd

df = pd.DataFrame(pd.read_table('RAW_OutsideDBs_class.tsv'))

#First sort to find top result for sequence ID
df2 = df.groupby(["SeqID"]).first()
df2 = df2.sort_values("EValue").drop(columns="Unnamed: 0").reset_index()
df2.to_csv("RAW_OutsideDBs_hits.tsv", sep = "\t")


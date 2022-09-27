import pandas as pd

df = pd.DataFrame(pd.read_table('evalue_taxonomy_i3.tsv'))

topHits_df = pd.DataFrame(columns=['GenomeID', 
    'nifH', 'EV_nifH', 'bitscore_nifH', 
    'nifD', 'EV_nifD', 'bitscore_nifD',
    'nifK', 'EV_nifK', 'bitscore_nifK',
    'anfH', 'EV_anfH', 'bitscore_anfH',
    'anfD', 'EV_anfD', 'bitscore_anfD',
    'anfK', 'EV_anfK', 'bitscore_anfK',
    'vnfH', 'EV_vnfH', 'bitscore_vnfH',
    'vnfD', 'EV_vnfD', 'bitscore_vnfD',
    'vnfK', 'EV_vnfK', 'bitscore_vnfK',
    'nflD', 'EV_nflD', 'bitscore_nflD',
    'nflH', 'EV_nflH', 'bitscore_nflH',
    'ChlN', 'EV_ChlN', 'bitscore_ChlN',
    'ChIl', 'EV_ChIl', 'bitscore_ChIl',
    'ChlB', 'EV_ChlB', 'bitscore_ChlB',
    'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax'])

#Group by SeqID and grab the first entry (highest E-value)
df2 = df.groupby("SeqID").first()
df2 = df2.reset_index()
df2 = df2.sort_values("Bitscore")

#Loop through top hits dataframe to put it in the dictionary in the corressponding columns
for index, row in df2.iterrows():
    topHits_df['GenomeID'] = df2['GenomeID']
    for col in topHits_df.columns:
        if row['GeneName'] == col:
            ev = "EV_" + col
            bs = "bitscore_" + col
            topHits_df.loc[topHits_df.GenomeID == row['GenomeID'], [col, ev, bs, 'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax']] = row['SeqID'], row['EValue'], row['Bitscore'], row['GTDB_Tax'], row['NCBI_TaxID'], row['NCBI_Tax']

#Drop duplicates and make a TSV
topHits_df = topHits_df.drop_duplicates()
topHits_df.to_csv("tophits_i3.tsv", sep = "\t")


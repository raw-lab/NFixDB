import pandas as pd

df = pd.DataFrame(pd.read_table('evalue_taxonomy_i3.tsv'))

top_fasta = pd.DataFrame(columns=['GenomeID', 
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
    top_fasta['GenomeID'] = df2['GenomeID']
    for col in top_fasta.columns:
        if row['GeneName'] == col:
            if row['EValue'] < 9.9e-15 or row['Bitscore'] > 50:
                ev = "EV_" + col
                bs = "bitscore_" + col
                top_fasta.loc[top_fasta.GenomeID == row['GenomeID'], [col, ev, bs, 'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax']] = row['SeqID'], row['EValue'], row['Bitscore'], row['GTDB_Tax'], row['NCBI_TaxID'], row['NCBI_Tax']

#Drop duplicates and make a TSV
top_fasta = top_fasta.drop_duplicates().dropna(thresh=7)
top_fasta.to_csv("topfasta_i3.tsv", sep = "\t")


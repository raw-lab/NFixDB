import pandas as pd

df = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/ar53_metadata_r214.tsv'))
df2 = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/bac120_metadata_r214.tsv'))

frame = [df, df2]
complete_df = pd.concat(frame)

complete_df = complete_df[['gtdb_genome_representative', 'gtdb_taxonomy', 'ncbi_taxid', 'ncbi_taxonomy_unfiltered']].copy()
complete_df.columns = ['GenomeID', 'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax']
complete_df.to_csv("complete_taxonomy.tsv", sep = "\t")
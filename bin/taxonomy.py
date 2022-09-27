import pandas as pd
from Bio import SearchIO
import os
import re
import sqlite3


conn = sqlite3.connect('NFixDB')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS nitrogenase_i3 (GenomeID varchar, SeqID varchar, EValue float, BitScore float, GeneName varchar, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
conn.commit()

c.execute('CREATE TABLE IF NOT EXISTS nonNitrogenase_i3 (GenomeID varchar, SeqID varchar, EValue float, BitScore float, GeneName varchar, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
conn.commit()
'''
df = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/ar53_metadata_r207.tsv'))
df2 = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/bac120_metadata_r207.tsv'))

frame = [df, df2]
complete_df = pd.concat(frame)

complete_df = complete_df[['gtdb_genome_representative', 'gtdb_taxonomy', 'ncbi_taxid', 'ncbi_taxonomy_unfiltered']].copy()
complete_df.columns = ['GenomeID', 'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax']
complete_df.to_csv("complete_taxonomy.tsv", sep = "\t")
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

complete_df = pd.DataFrame(pd.read_table('complete_taxonomy.tsv'))

result_target = []
query_id = []
hit_id = []
evalue = []
bitscore = []

#OOR stands for "Out Of Range", AKA the values that do not meet our E-value threshold
oor_target = []
oor_queryid = []
oor_hitid = []
oor_evalue = []
oor_bitscore = []

#parse through files in output directory
directory = 'bac120_ar53_results_i3' 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    reg = r'^([\w]+_[\w]+.[\w])'
    regex = re.match(reg, filename).group()
    if os.path.isfile(f):
        #parse file using SearchIO/HmmerIO
        for result in SearchIO.parse(f, 'hmmer3-text'):
            for item in result.hits:
                reg2 = r'([a-zA-Z]+)_([a-zA-Z]+)-([a-zA-Z]+)_([a-zA-Z]+)'
                regex2 = re.match(reg2, result.id).group(2)
                #check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10:
                    result_target.append(regex)
                    query_id.append(regex2)
                    hit_id.append(item.id)
                    evalue.append(item.evalue)
                    bitscore.append(item.bitscore)
                #if it does not meet the evalue cutoff, append it to the OOR lists
                else:
                    oor_target.append(regex)
                    oor_queryid.append(regex2)
                    oor_hitid.append(item.id)
                    oor_evalue.append(item.evalue)
                    oor_bitscore.append(item.bitscore)

evalue_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')
evalue_df = pd.merge(evalue_df, complete_df, on = "GenomeID", how = "left")

oor_dict = {'GenomeID' : oor_target, 'GeneName' : oor_queryid, 'SeqID' : oor_hitid, 'EValue' : oor_evalue, 'Bitscore' : oor_bitscore}
oor_df = pd.DataFrame(oor_dict).sort_values('EValue')
oor_df = pd.merge(oor_df, complete_df, on = "GenomeID", how = "left")

evalue_df.to_csv("evalue_taxonomy_i3.tsv", sep = "\t")
evalue_df.to_sql('nitrogenase_i3', conn, if_exists = 'replace')

oor_df.to_csv("oor_taxonomy_i3.tsv", sep = "\t")
oor_df.to_sql('nonNitrogenase_i3', conn, if_exists = 'replace', index = False)

'''
c.execute("SELECT * FROM nitrogenase")
for row in c.fetchall():
    print(row)

c.execute("SELECT * FROM nonNitrogenase")
for row in c.fetchall():
    print(row)

print(evalue_df)
print()
print(oor_df)'''

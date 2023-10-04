import pandas as pd
from Bio import SearchIO
import os
import re

'''
df = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/ar53_metadata_r214.tsv'))
df2 = pd.DataFrame(pd.read_table('/projects/raw_lab/databases/GTDB/bac120_metadata_r214.tsv'))

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
location = []
alength = []
slength = []

'''
#OOR stands for "Out Of Range", AKA the values that do not meet our E-value threshold
oor_target = []
oor_queryid = []
oor_hitid = []
oor_evalue = []
oor_bitscore = []'''

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
                reg2 = r'([a-zA-Z]+)-([a-zA-Z]+)'
                regex2 = re.match(reg2, result.id).group(1)
                #check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10:
                    result_target.append(regex)
                    query_id.append(regex2)
                    hit_id.append(item.id)
                    evalue.append(item.evalue)
                    bitscore.append(item.bitscore)
                    reg3 = r'# ([0-9]+) # ([0-9]+)'
                    location.append(re.match(reg3, item.description).group(1) + "-" + re.match(reg3, item.description).group(2))
                    alength.append(item.hsps[0].aln_span)
                    slength.append(int(re.match(reg3, item.description).group(2))-int(re.match(reg3, item.description).group(1)))
                #if it does not meet the evalue cutoff, append it to the OOR lists
                '''else:
                    oor_target.append(regex)
                    oor_queryid.append(regex2)
                    oor_hitid.append(item.id)
                    oor_evalue.append(item.evalue)
                    oor_bitscore.append(item.bitscore)'''

evalue_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 
               'Location' : location, 'AlnLength' : alength, 'SeqLength' : slength}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')
evalue_df = pd.merge(evalue_df, complete_df, on = "GenomeID", how = "left").drop(columns = ["Unnamed: 0"]).drop_duplicates()

evalue_df.to_csv("evalue_taxonomy_i3.tsv", sep = "\t")

'''
oor_dict = {'GenomeID' : oor_target, 'GeneName' : oor_queryid, 'SeqID' : oor_hitid, 'EValue' : oor_evalue, 'Bitscore' : oor_bitscore}
oor_df = pd.DataFrame(oor_dict).sort_values('EValue')
oor_df = pd.merge(oor_df, complete_df, on = "GenomeID", how = "left")

oor_df.to_csv("oor_taxonomy_i3.tsv", sep = "\t")
'''


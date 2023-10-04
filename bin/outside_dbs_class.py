import pandas as pd
from Bio import SearchIO
import os
import re

db = []
query_id = []
hit_id = []
evalue = []
bitscore = []
alength = []

#parse through files in output directory
directory = 'outside_dbs_results' 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    reg = r'^([\w]+)_(([\w]+)-([\w]+))'
    regex = re.match(reg, filename).group(2)
    if os.path.isfile(f):
        #parse file using SearchIO/HmmerIO
        for result in SearchIO.parse(f, 'hmmer3-text'):
            for item in result.hits:
                reg2 = r'([a-zA-Z]+)-([a-zA-Z]+)'
                regex2 = re.match(reg2, result.id).group(1)
                #check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10:
                    db.append(regex)
                    query_id.append(regex2)
                    hit_id.append(item.id)
                    evalue.append(item.evalue)
                    bitscore.append(item.bitscore)
                    alength.append(item.hsps[0].aln_span)

evalue_dict = {'Database' : db, 'Gene' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 'AlnLength' : alength}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')

evalue_df.to_csv("RAW_OutsideDBs_class.tsv", sep = "\t")

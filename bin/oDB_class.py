import pandas as pd
from Bio import SearchIO
import os
import re

db = []
ogene = []
query_id = []
hit_id = []
evalue = []
bitscore = []
alength = []

#parse through files in output directory
directory = 'oDB_results/clusters' 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # RegEx for database name
    reg = r'([^_]*)'
    regex = re.match(reg, filename).group(1)
    # RegEx for original gene
    reg2 = r'\_(.*?)\_'
    regex2 = re.search(reg2, filename).group(1)
    print("Analyzing " + regex2 + " in " + filename)
    if os.path.isfile(f):
        #parse file using SearchIO/HmmerIO
        for result in SearchIO.parse(f, 'hmmer3-text'):
            for item in result.hits:
                reg3 = r'([a-zA-Z]+)-([a-zA-Z]+)'
                regex3 = re.match(reg3, result.id).group(1)
                #check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10 and item.hsps[0].aln_span > 150:
                    db.append(regex)
                    ogene.append(regex2)
                    query_id.append(regex3)
                    hit_id.append(item.id)
                    evalue.append(item.evalue)
                    bitscore.append(item.bitscore)
                    alength.append(item.hsps[0].aln_span)

evalue_dict = {'Database' : db, 'OrgGene' : ogene, 'Gene' : query_id, 'SeqID' : hit_id, 'EValue' : evalue, 'Bitscore' : bitscore, 'AlnLength' : alength}
evalue_df = pd.DataFrame(evalue_dict).sort_values('EValue')

evalue_df.to_csv("TSVs/oDB_class.tsv", sep = "\t")

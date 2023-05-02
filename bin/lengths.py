import os
import pandas as pd
from Bio import SearchIO
import re
import csv

result_target = []
query_id = []
hit_id = []
length = []

#parse through files in output directory
directory = 'bac120_ar53_results_i3' 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    reg = r'([A-Z]+_[0-9]+.[0-9])'
    regex = re.search(reg, filename).group()
    if os.path.isfile(f):
        #parse file using SearchIO/HmmerIO
        for result in SearchIO.parse(f, 'hmmer3-text'):
            for item in result.hits:
                reg2 = r'^([\w]+)'
                regex2 = re.match(reg2, result.id).group()
                #check the evalue cutoff and append the data to the corresponding lists
                if item.evalue < 9.9e-10:
                    result_target.append(regex)
                    query_id.append(regex2)
                    hit_id.append(item.id)
                    length.append(item.hsps[0].aln_span)

alnlength_dict = {'GenomeID' : result_target, 'GeneName' : query_id, 'SeqID' : hit_id, 'AlnLength' : length}
alnlength_df = pd.DataFrame(alnlength_dict)


genid = []
seqid = []
seqlen = []

directory = 'lengths'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    reg = r'([A-Z]+_[0-9]+.[0-9])'
    regex = re.search(reg, filename).group()
    if os.path.isfile(f):
        with open(f, 'r') as fi:
            reader = csv.reader(fi, delimiter='\t')
            for seq, lenth in reader:
                genid.append(regex)
                seqid.append(seq)
                seqlen.append(lenth)

seqlength_dict = {'GenomeID' : genid, 'SeqID' : seqid, 'SeqLength' : seqlen}
seqlength_df = pd.DataFrame(seqlength_dict)

lengths_df = pd.merge(alnlength_df, seqlength_df, on=['GenomeID', 'SeqID'], how='left')

lengths_df.to_csv("lengths_i3.tsv", sep = "\t")

eval_df = pd.DataFrame(pd.read_table("TSVs/evalue_taxonomy_i3.tsv"))
final_df = pd.merge(eval_df, lengths_df, on=['GenomeID', 'GeneName', 'SeqID'], how='left').drop_duplicates().drop(columns=['Unnamed: 0'])

complete_df = pd.DataFrame(pd.read_table('TSVs/complete_taxonomy.tsv'))

final_df = pd.merge(final_df, complete_df, on = "GenomeID", how = "left").drop(columns=['Unnamed: 0'])

final_df.to_csv("evalue_wLen_i3.tsv", sep = "\t")

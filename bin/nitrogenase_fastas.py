from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os
import re

df = pd.DataFrame(pd.read_table('TSVs/filteredfasta_i2-3.tsv'))

nifD = []
nifH = []
nifK = [] 
anfD = []
anfH = []
anfK = []
vnfD = []
vnfH = []
vnfK = []
nflD = []
nflH = []
ChlN = [] 
ChIl = []
ChlB = []

directory = '/projects/raw_lab/databases/GTDB/protein_faa_reps_r214-combined' 
for index, row in df.iterrows():
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        if os.path.isfile(f):
            reg = r'^([\w]+_[\w]+.[\w])'
            regex = re.match(reg, file).group()
            if regex == row['GenomeID']:
                for fasta in SeqIO.parse(f, 'fasta'):
                    if fasta.id == row['nifD']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        nifD.append(rec)
                    elif fasta.id == row['nifH']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        nifH.append(rec)
                    elif fasta.id == row['nifK']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        nifK.append(rec)
                    elif fasta.id == row['anfD']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        anfD.append(rec)
                    elif fasta.id == row['anfK']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        anfK.append(rec)
                    elif fasta.id == row['anfH']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        anfH.append(rec)
                    elif fasta.id == row['vnfD']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        vnfD.append(rec)
                    elif fasta.id == row['vnfK']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        vnfK.append(rec)
                    elif fasta.id == row['vnfH']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        vnfH.append(rec)
                    elif fasta.id == row['nflD']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        nflD.append(rec)
                    elif fasta.id == row['nflH']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        nflH.append(rec)
                    elif fasta.id == row['ChlN']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        ChlN.append(rec)
                    if fasta.id == row['ChIl']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        ChIl.append(rec)
                    elif fasta.id == row['ChlB']:
                        rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                        ChlB.append(rec)

path = os.path.abspath("fastas/R2/final")
if not os.path.exists(path):
    os.makedirs(path)

SeqIO.write(nifD, path+"/nifD_01032024.faa", "fasta") 
SeqIO.write(nifH, path+"/nifH_01032024.faa", "fasta")
SeqIO.write(nifK, path+"/nifK_01032024.faa", "fasta")

SeqIO.write(anfD, path+"/anfD_01032024.faa", "fasta")
SeqIO.write(anfH, path+"/anfH_01032024.faa", "fasta")
SeqIO.write(anfK, path+"/anfK_01032024.faa", "fasta")

SeqIO.write(vnfD, path+"/vnfD_01032024.faa", "fasta")
SeqIO.write(vnfH, path+"/vnfH_01032024.faa", "fasta")
SeqIO.write(vnfK, path+"/vnfK_01032024.faa", "fasta")

SeqIO.write(nflD, path+"/nflD_01032024.faa", "fasta")
SeqIO.write(nflH, path+"/nflH_01032024.faa", "fasta")

SeqIO.write(ChlN, path+"/ChlN_01032024.faa", "fasta")
SeqIO.write(ChIl, path+"/ChIl_01032024.faa", "fasta")
SeqIO.write(ChlB, path+"/ChlB_01032024.faa", "fasta") 

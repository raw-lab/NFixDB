#!/usr/bin/python3

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='results/i1/TSVs/filteredfasta.tsv', help="Path to filteredfasta.tsv")
parser.add_argument('-o', '--output', type=str, default='results/i1/fasta', help="Path to the output folder to save fasta files")
parser.add_argument('-g', '--gtdb', type=str, help="Path to the GTDB folder", required=True)

args = parser.parse_args()


# Get filteredfasta TSV
df = pd.DataFrame(pd.read_table(args.input))

# Make empty lists for each fasta
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

# Create fasta lists by column name
directory = args.gtdb
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

path = os.path.abspath(args.output)
if not os.path.exists(path):
    os.makedirs(path)

# Make actual fasta files
SeqIO.write(nifD, path+"/nifD_01052024.faa", "fasta") 
SeqIO.write(nifH, path+"/nifH_01052024.faa", "fasta")
SeqIO.write(nifK, path+"/nifK_01052024.faa", "fasta")

SeqIO.write(anfD, path+"/anfD_01052024.faa", "fasta")
SeqIO.write(anfH, path+"/anfH_01052024.faa", "fasta")
SeqIO.write(anfK, path+"/anfK_01052024.faa", "fasta")

SeqIO.write(vnfD, path+"/vnfD_01052024.faa", "fasta")
SeqIO.write(vnfH, path+"/vnfH_01052024.faa", "fasta")
SeqIO.write(vnfK, path+"/vnfK_01052024.faa", "fasta")

SeqIO.write(nflD, path+"/nflD_01052024.faa", "fasta")
SeqIO.write(nflH, path+"/nflH_01052024.faa", "fasta")

SeqIO.write(ChlN, path+"/ChlN_01052024.faa", "fasta")
SeqIO.write(ChIl, path+"/ChIl_01052024.faa", "fasta")
SeqIO.write(ChlB, path+"/ChlB_01052024.faa", "fasta") 

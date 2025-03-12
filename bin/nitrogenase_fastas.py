#!/usr/bin/python3

import argparse
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os
import re
import gzip

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='results/i1/TSVs/filteredfasta.tsv', help="Path to filteredfasta.tsv")
parser.add_argument('-o', '--output', type=str, default='results/i1/fasta', help="Path to the output folder to save fasta files")
parser.add_argument('-g', '--gtdb', type=str, help="Path to the GTDB folder", required=True)

args = parser.parse_args()


# Get filteredfasta TSV
df = pd.DataFrame(pd.read_table(args.input))

path = os.path.abspath(args.output)
if not os.path.exists(path):
    os.makedirs(path)

# Open file handles for output files
h_nifD = open(path+"/nifD.faa", "w")
h_nifH = open(path+"/nifH.faa", "w")
h_nifK = open(path+"/nifK.faa", "w")
h_anfD = open(path+"/anfD.faa", "w")
h_anfH = open(path+"/anfH.faa", "w")
h_anfK = open(path+"/anfK.faa", "w")
h_vnfD = open(path+"/vnfD.faa", "w")
h_vnfH = open(path+"/vnfH.faa", "w")
h_vnfK = open(path+"/vnfK.faa", "w")
h_nflD = open(path+"/nflD.faa", "w")
h_nflH = open(path+"/nflH.faa", "w")
h_ChlN = open(path+"/ChlN.faa", "w")
h_ChIl = open(path+"/ChIl.faa", "w")
h_ChlB = open(path+"/ChlB.faa", "w")

reg = re.compile(r'^([\w]+_[\w]+.[\w])')

# Create fasta lists by column name
directory = args.gtdb
for file in os.listdir(f"{directory}/archaea") + os.listdir(f"{directory}/bacteria"):
    if Path(directory, "archaea", file).exists():
        f = Path(directory, "archaea", file)
    elif Path(directory, "bacteria", file).exists():
        f = Path(directory, "bacteria", file)
    else:
        print("ERROR:", file)
        continue

    regex = reg.match(file).group()
    matches = df.loc[df['GenomeID'] == regex]
    for index, row in matches.iterrows():
        if regex == row['GenomeID']:
            if f.suffix.endswith('.gz'):
                f_handle = gzip.open(f, "rt")
            else:
                f_handle = open(f)
            for fasta in SeqIO.parse(f_handle, 'fasta'):
                if fasta.id == row['nifD']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_nifD, "fasta")
                elif fasta.id == row['nifH']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_nifH, "fasta")
                elif fasta.id == row['nifK']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_nifK, "fasta")
                elif fasta.id == row['anfD']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_anfD, "fasta")
                elif fasta.id == row['anfK']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_anfK, "fasta")
                elif fasta.id == row['anfH']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_anfH, "fasta")
                elif fasta.id == row['vnfD']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_vnfD, "fasta")
                elif fasta.id == row['vnfK']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_vnfK, "fasta")
                elif fasta.id == row['vnfH']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_vnfH, "fasta")
                elif fasta.id == row['nflD']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_nflD, "fasta")
                elif fasta.id == row['nflH']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_nflH, "fasta")
                elif fasta.id == row['ChlN']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_ChlN, "fasta")
                elif fasta.id == row['ChIl']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_ChIl, "fasta")
                elif fasta.id == row['ChlB']:
                    rec = SeqRecord(Seq(str(fasta.seq)), id=fasta.id, description=fasta.description)
                    SeqIO.write(rec, h_ChlB, "fasta")
            f_handle.close()

# Close file handles
h_nifD.close()
h_nifH.close()
h_nifK.close()
h_anfD.close()
h_anfH.close()
h_anfK.close()
h_vnfD.close()
h_vnfH.close()
h_vnfK.close()
h_nflD.close()
h_nflH.close()
h_ChlN.close()
h_ChIl.close()
h_ChlB.close()


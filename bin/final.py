import pandas as pd

tophits = pd.DataFrame(pd.read_table('TSVs/tophits_i3.tsv'))
taxid = tophits[['GenomeID', 'NCBI_TaxID']]

lengths = pd.DataFrame(pd.read_table('lengths_i3.tsv'))
lens = pd.DataFrame(columns=['GenomeID', 'nifH', 'alnLen_nifH', 'seqLen_nifH',
                             'nifD', 'alnLen_nifD', 'seqLen_nifD',
                             'nifK', 'alnLen_nifK', 'seqLen_nifK',
                             'anfH', 'alnLen_anfH', 'seqLen_anfH',
                             'anfD', 'alnLen_anfD', 'seqLen_anfD',
                             'anfK', 'alnLen_anfK', 'seqLen_anfK',
                             'vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
                             'vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
                             'vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
                             'nflH', 'alnLen_nflH', 'seqLen_nflH',
                             'nflD', 'alnLen_nflD', 'seqLen_nflD',
                             'ChlB', 'alnLen_ChlB', 'seqLen_ChlB',
                             'ChIl', 'alnLen_ChIl', 'seqLen_ChIl',
                             'ChlN', 'alnLen_ChlN', 'seqLen_ChlN'])

for index, row in lengths.iterrows():
    lens['GenomeID'] = lengths['GenomeID']
    for col in lens.columns:
        if row['GeneName'] == col:
            al = "alnLen_" + col
            sl = "seqLen_" + col
            lens.loc[lens.GenomeID == row['GenomeID'], [col, al, sl]] = row['SeqID'], row['AlnLength'], row['SeqLength']
lens = lens.drop_duplicates()

filthits = pd.DataFrame(pd.read_table('filteredhits_i3_wSSU.tsv'))

final = pd.merge(filthits, taxid, on='GenomeID', how="left").drop(columns=["Unnamed: 0.1", "Unnamed: 0"])
final = pd.merge(final, lens, on=['GenomeID', 'nifH', 'nifD', 'nifK', 'anfH', 
                                  'anfD', 'anfK', 'vnfH', 'vnfD', 'vnfK', 'nflH', 
                                  'nflD', 'ChlB', 'ChIl', 'ChlN'], how="left")

final = final[['GenomeID', 'nifH', 'EV_nifH', 'bitscore_nifH', 'alnLen_nifH', 'seqLen_nifH',
                            'nifD', 'EV_nifD', 'bitscore_nifD', 'alnLen_nifD', 'seqLen_nifD',
                            'nifK', 'EV_nifK', 'bitscore_nifK', 'alnLen_nifK', 'seqLen_nifK',
                            'anfH', 'EV_anfH', 'bitscore_anfH', 'alnLen_anfH', 'seqLen_anfH',
                            'anfD', 'EV_anfD', 'bitscore_anfD', 'alnLen_anfD', 'seqLen_anfD',
                            'anfK', 'EV_anfK', 'bitscore_anfK', 'alnLen_anfK', 'seqLen_anfK',
                            'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
                            'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
                            'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
                            'nflH', 'EV_nflH', 'bitscore_nflH', 'alnLen_nflH', 'seqLen_nflH',
                            'nflD', 'EV_nflD', 'bitscore_nflD', 'alnLen_nflD', 'seqLen_nflD',
                            'ChlB', 'EV_ChlB', 'bitscore_ChlB', 'alnLen_ChlB', 'seqLen_ChlB',
                            'ChIl', 'EV_ChIl', 'bitscore_ChIl', 'alnLen_ChIl', 'seqLen_ChIl',
                            'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',
                            'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax', '5S', '5.8S', '16S', '23S']]

final.to_csv("NFixDB.tsv", sep="\t")  

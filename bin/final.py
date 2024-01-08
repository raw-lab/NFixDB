import pandas as pd

tophits = pd.DataFrame(pd.read_table('TSVs/tophits_i2-3.tsv'))
taxid = tophits[['GenomeID', 'NCBI_TaxID', 'location_nflH', 'location_nflD', 
                'location_ChlB', 'location_ChIl', 'location_ChlN']]

filthits = pd.DataFrame(pd.read_table('TSVs/filteredhits_SSU_i2-3.tsv'))

final = pd.merge(filthits, taxid, on='GenomeID', how="left").drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

final = final[['GenomeID', 'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
                            'nifD', 'EV_nifD', 'bitscore_nifD', 'location_nifD', 'alnLen_nifD', 'seqLen_nifD',
                            'nifK', 'EV_nifK', 'bitscore_nifK', 'location_nifK', 'alnLen_nifK', 'seqLen_nifK',
                            'anfH', 'EV_anfH', 'bitscore_anfH', 'location_anfH', 'alnLen_anfH', 'seqLen_anfH',
                            'anfD', 'EV_anfD', 'bitscore_anfD', 'location_anfD', 'alnLen_anfD', 'seqLen_anfD',
                            'anfK', 'EV_anfK', 'bitscore_anfK', 'location_anfK', 'alnLen_anfK', 'seqLen_anfK',
                            'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'location_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
                            'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'location_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
                            'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'location_vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
                            'nflH', 'EV_nflH', 'bitscore_nflH', 'location_nflH', 'alnLen_nflH', 'seqLen_nflH',
                            'nflD', 'EV_nflD', 'bitscore_nflD', 'location_nflD', 'alnLen_nflD', 'seqLen_nflD',
                            'ChlB', 'EV_ChlB', 'bitscore_ChlB', 'location_ChlB', 'alnLen_ChlB', 'seqLen_ChlB',
                            'ChIl', 'EV_ChIl', 'bitscore_ChIl', 'location_ChIl', 'alnLen_ChIl', 'seqLen_ChIl',
                            'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'location_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',
                            'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax', '5S', '5.8S', '16S', '23S']]

final.to_csv("TSVs/NFixDB-R2.tsv", sep="\t")  

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='results/i1/TSVs/filteredhits_SSU.tsv', help="Path to filteredhits_SSU.tsv")
parser.add_argument('-o', '--output', type=str, default='results/i1/TSVs/NFixDB.tsv', help="Path to the final TSV file NFixDB.tsv")

args = parser.parse_args()

filthits = pd.DataFrame(pd.read_table(args.input))

final = filthits[['GenomeID', 'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
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

final.to_csv(args.output, sep="\t", index=False)

import pandas as pd

df = pd.DataFrame(pd.read_table('results/TSVs/topfasta.tsv'))
print("fasta counts: ")

#nifHDK
nif = df[['GenomeID', 
          'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
          'nifD', 'EV_nifD', 'bitscore_nifD', 'location_nifD', 'alnLen_nifD', 'seqLen_nifD',
          'nifK', 'EV_nifK', 'bitscore_nifK', 'location_nifK', 'alnLen_nifK', 'seqLen_nifK']].copy()
nif = nif.dropna().reset_index()
print("nifHDK: " + str(len(nif)))

#vnfHDK
vnf = df[['GenomeID', 
          'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'location_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
          'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'location_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
          'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'location_vnfK', 'alnLen_vnfK', 'seqLen_vnfK']].copy()
vnf = vnf.dropna().reset_index()
print("vnfHDK: " + str(len(vnf)))

#anfHDK
anf = df[['GenomeID', 
          'anfH', 'EV_anfH', 'bitscore_anfH', 'location_anfH', 'alnLen_anfH', 'seqLen_anfH',
          'anfD', 'EV_anfD', 'bitscore_anfD', 'location_anfD', 'alnLen_anfD', 'seqLen_anfD',
          'anfK', 'EV_anfK', 'bitscore_anfK', 'location_anfK', 'alnLen_anfK', 'seqLen_anfK']].copy()
anf = anf.dropna().reset_index()
print("anfHDK: " + str(len(anf)))

#nfl
n = df[['GenomeID', 
        'nflD', 'EV_nflD', 'bitscore_nflD', 'location_nflD', 'alnLen_nflD', 'seqLen_nflD',
        'nflH', 'EV_nflH', 'bitscore_nflH', 'location_nflH', 'alnLen_nflH', 'seqLen_nflH']].copy()
n = n.dropna().reset_index()
print("nflHD: " + str(len(n)))

#Chl
c = df[['GenomeID', 
        'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'location_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',
        'ChIl', 'EV_ChIl', 'bitscore_ChIl', 'location_ChIl', 'alnLen_ChIl', 'seqLen_ChIl',
        'ChlB', 'EV_ChlB', 'bitscore_ChlB', 'location_ChlB', 'alnLen_ChlB', 'seqLen_ChlB']].copy()
c = c.dropna().reset_index()
print("ChlNIB: " + str(len(c)))

nav = df[['GenomeID', 
          'nifH', 'nifD', 'nifK',
          'anfD', 'anfH', 'anfK',
          'vnfD', 'vnfH', 'vnfK']].copy()

nav = nav.dropna().reset_index()
print("nif, vnf, and anf: " + str(len(nav)))

dfs = [df.set_index(['GenomeID']) for df in [nif, vnf, anf, n, c]]
merged_df = pd.concat(dfs, axis=1).drop(columns="index")

merged_df.to_csv("results/TSVs/filteredfasta.tsv", sep="\t", index=True, index_label="GenomeID")

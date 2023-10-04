import pandas as pd

df = pd.DataFrame(pd.read_table('tophits_i3.tsv'))

#nifHDK
nif = df[['GenomeID', 
          'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
          'nifD', 'EV_nifD', 'bitscore_nifD', 'location_nifD', 'alnLen_nifD', 'seqLen_nifD',
          'nifK', 'EV_nifK', 'bitscore_nifK', 'location_nifK', 'alnLen_nifK', 'seqLen_nifK',
          'GTDB_Tax', 'NCBI_Tax']].copy()

nif = nif.dropna().reset_index()
print("nifHDK: " + str(len(nif)))

#vnfHDK
vnf = df[['GenomeID', 
          'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'location_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
          'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'location_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
          'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'location_vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
          'GTDB_Tax', 'NCBI_Tax']].copy()

vnf = vnf.dropna().reset_index()
print("vnf: " + str(len(vnf)))

#anfHDK
anf = df[['GenomeID', 
          'anfH', 'EV_anfH', 'bitscore_anfH', 'location_anfH', 'alnLen_anfH', 'seqLen_anfH',
          'anfD', 'EV_anfD', 'bitscore_anfD', 'location_anfD', 'alnLen_anfD', 'seqLen_anfD',
          'anfK', 'EV_anfK', 'bitscore_anfK', 'location_anfK', 'alnLen_anfK', 'seqLen_anfK',
          'GTDB_Tax', 'NCBI_Tax']].copy()

anf = anf.dropna().reset_index()
print("anf: " + str(len(anf)))

#nif, vnf, anf
nav = df[['GenomeID', 
          'nifH', 'EV_nifH', 'nifD', 'EV_nifD', 'nifK', 'EV_nifK',
          'anfD', 'EV_anfD', 'anfH', 'EV_anfH', 'anfK', 'EV_anfK',
          'vnfD', 'EV_vnfD', 'vnfH', 'EV_vnfH', 'vnfK', 'EV_vnfK', 
          'GTDB_Tax', 'NCBI_Tax']].copy()

nav = nav.dropna().reset_index()
print("nif, vnf, and anf: " + str(len(nav)))

#nfl
n = df[['GenomeID', 
        'nflD', 'EV_nflD', 'bitscore_nflD',
        'nflH', 'EV_nflH', 'bitscore_nflH',
        'GTDB_Tax', 'NCBI_Tax']].copy()

n = n.dropna().reset_index()
print("nfl: " + str(len(n)))

#Chl
c = df[['GenomeID', 
        'ChlN', 'EV_ChlN', 'bitscore_ChlN',
        'ChIl', 'EV_ChIl', 'bitscore_ChIl',
        'ChlB', 'EV_ChlB', 'bitscore_ChlB',
        'GTDB_Tax', 'NCBI_Tax']].copy()

c = c.dropna().reset_index()
print("Chl: " + str(len(c)))

#all of them
all = df[['GenomeID', 
          'nifD', 'nifH', 'nifK',
          'anfD', 'anfH', 'anfK',
          'vnfD', 'vnfH', 'vnfK',
          'nflD', 'nflH',
          'ChlN', 'ChIl', 'ChlB']].copy()

all = all.dropna().reset_index()
print("All: " + str(len(all)))

dfs = [df.set_index(['GenomeID', 'GTDB_Tax', 'NCBI_Tax']) for df in [nif, vnf, anf, n, c]]
merged_df = pd.concat(dfs, axis=1).reset_index().drop(columns="index")

merged_df.to_csv("filteredhits_i3.tsv", sep="\t")



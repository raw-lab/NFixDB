import pandas as pd

df = pd.DataFrame(pd.read_table('topfasta_i3.tsv'))

#nifHDK: 1650
nifHDK = df[['GenomeID', 'nifH', 'nifD','nifK']].copy()

nifHDK = nifHDK.dropna().reset_index()
print("nifHDK: " + str(len(nifHDK)))

#all of them: 0
all = df[['GenomeID', 
        'nifD', 'nifH', 'nifK',
        'anfD', 'anfH', 'anfK',
        'vnfD', 'vnfH', 'vnfK',
        'nflD', 'nflH',
        'ChlN', 'ChIl', 'ChlB']].copy()

all = all.dropna().reset_index()
print("All: " + str(len(all)))

#nif, vnf, anf: 2
nav = df[['GenomeID', 
        'nifD', 'nifH', 'nifK',
        'anfD', 'anfH', 'anfK',
        'vnfD', 'vnfH', 'vnfK', 'GTDB_Tax', 'NCBI_Tax']].copy()

nav = nav.dropna().reset_index()
print("nif, vnf, and anf: " + str(len(nav)))

#Chl: 2616
c = df[['GenomeID', 
        'ChlN', 'ChIl', 'ChlB']].copy()

c = c.dropna().reset_index()
print("Chl: " + str(len(c)))

#vnfHDK: 86
vnfDH = df[['GenomeID', 
        'vnfD', 'vnfH', 'vnfK']].copy()

vnfDH = vnfDH.dropna().reset_index()
print("vnf: " + str(len(vnfDH)))

#206
anfDH = df[['GenomeID', 
        'anfD', 'anfH', 'anfK']].copy()

anfDH = anfDH.dropna().reset_index()
print("anf: " + str(len(anfDH)))


#581
n = df[['GenomeID', 
        'nflD', 'nflH']].copy()

n = n.dropna().reset_index()
print("nfl: " + str(len(n)))


dfs = [df.set_index(['GenomeID']) for df in [nifHDK, vnfDH, anfDH, n, c]]
merged_df = pd.concat(dfs, axis=1).reset_index().drop(columns="index")
print(merged_df)
merged_df.to_csv("mergefasta_i3.tsv", sep="\t")

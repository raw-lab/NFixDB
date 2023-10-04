import pandas as pd

df = pd.DataFrame(pd.read_table('topfasta_i3.tsv'))
print("fasta counts: ")

#nifHDK
nif = df[['GenomeID', 'nifH', 'nifD', 'nifK']].copy()
nif = nif.dropna().reset_index()
print("nifHDK: " + str(len(nif)))

#vnfHDK
vnf = df[['GenomeID', 'vnfH', 'vnfD', 'vnfK']].copy()
vnf = vnf.dropna().reset_index()
print("vnfHDK: " + str(len(vnf)))

#anfHDK
anf = df[['GenomeID', 'anfH', 'anfD', 'anfK']].copy()
anf = anf.dropna().reset_index()
print("anfHDK: " + str(len(anf)))

#nfl
n = df[['GenomeID', 'nflD', 'nflH']].copy()
n = n.dropna().reset_index()
print("nflHD: " + str(len(n)))

#Chl
c = df[['GenomeID', 'ChlN', 'ChIl', 'ChlB']].copy()
c = c.dropna().reset_index()
print("ChlNIB: " + str(len(c)))

dfs = [df.set_index(['GenomeID']) for df in [nif, vnf, anf, n, c]]
merged_df = pd.concat(dfs, axis=1).reset_index().drop(columns="index")

merged_df.to_csv("filteredfasta_i3.tsv", sep="\t")

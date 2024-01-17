# Results 

### TSVs
+ **buckley_sword.tsv** - SWORD results from the Buckley database
+ **buckley_sword_hits.tsv** - top SWORD results from the Buckley database (AlnLength ≥ 220)
+ **evalue_taxonomy.tsv** - all sequences that meet ≤ e-10 cutoff (very large files,
  ***found on [Zenodo](https://doi.org/10.5281/zenodo.7887034)***)
+ **filteredhits.tsv** - genomes that have all three genes within a group (i.e. nifHDK) from tophits.tsv
+ **filteredfasta.tsv** - genomes that have all three genes within a group (i.e. nifHDK) from topfasta.tsv
+ **fungene_sword.tsv** - SWORD results from the FunGene nifH database
+ **fungene_sword_hits.tsv** - top SWORD results from the FunGene nifH database (AlnLength ≥ 220)
+ **mise_sword.tsv** - SWORD results from the Mise database
+ **mise_sword_hits.tsv** - top SWORD results from the Mise database (AlnLength ≥ 220)
+ **NFixDB-v2.tsv** - all results from iteration 3 compiled together
+ **NFixDB_Buckley_hits.tsv** - results from running our HMMs on Buckley's nifH database
+ **NFixDB_FunGene_hits.tsv** - results from running our HMMs on FunGene's nifH, nifD, and vnfD database
+ **NFixDB_Mise_hits.tsv** - results from running our HMMs on Mise's nifH database
+ **NFixDB_Zehr_hits.tsv** - results from running our HMMs on Zehr's nifH database
+ **oDB_class-97.tsv** - results from running our HMMs on all outside databases
+ **oDB_hits-97.tsv** - filtered results from running our HMMs on all outside databases
+ **topfasta.tsv** - top results of each gene from evalue_taxonomy.tsv that are within cutoff of ≤ e-15, bitscore of ≥ 50, or alignment length of > 125
+ **tophits.tsv** - top results of each gene from evalue_taxonomy.tsv. Zipped due to large size
+ **zehr_sword.tsv** - SWORD results from the Zehr database
+ **zehr_sword_hits.tsv** - top SWORD results from the Zehrs database (AlnLength ≥ 220)

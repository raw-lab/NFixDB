# Results 

### TSVs
+ **evalue_taxonomy(_i2-1, _i2-2 or _i2-3).tsv** - all sequences that meet ≤ e-10 cutoff (very large files,
  ***found on [Zenodo](https://doi.org/10.5281/zenodo.7887034)***)
+ **filteredhits(_i2-1, _i2-2 or _i2-3).tsv** - genomes that have all three genes within a group (i.e. nifHDK) from tophits.tsv
+ **filteredfasta(_i2-1, _i2-2 or _i2-3).tsv** - genomes that have all three genes within a group (i.e. nifHDK) from topfasta.tsv
+ **filteredhits_SSU_i2-3.tsv** - filteredhits_i2-3.tsv with SSU results from barrnap integrated
+ **NFixDB-v2.tsv** - all results from iteration 3 compiled together
+ **NFixDB_Buckley_hits.tsv** - results from running our HMMs on Buckley's nifH database
+ **NFixDB_FunGene_hits.tsv** - results from running our HMMs on FunGene's nifH, nifD, and vnfD database
+ **NFixDB_Mise_hits.tsv** - results from running our HMMs on Mise's nifH database
+ **oDB_class.tsv** - results from running our HMMs on all outside databases
+ **oDB_hits.tsv** - filtered results from running our HMMs on all outside databases
+ **NFixDB_Zehr_hits.tsv** - results from running our HMMs on Zehr's nifH database
+ **topfasta(_i2-1, _i2-2 or _i2-3).tsv** - top results of each gene from evalue_taxonomy.tsv that are within cutoff of ≤ e-15, bitscore of ≥ 50, or alignment length of > 125
+ **tophits(_i2-1, _i2-2 or _i2-3).tsv** - top results of each gene from evalue_taxonomy.tsv. Zipped due to large size

# Results 

### TSVs
+ **evalue_taxonomy(_i1, _i2 or _i3).tsv** - all sequences that meet ≤ e-10 cutoff (very large file, ***found on [Zenodo](https://doi.org/10.5281/zenodo.7887034)***)
+ **filteredhits(_i1, _i2 or _i3).tsv** - genomes that have all three genes within a group (i.e. nifHDK) from tophits.tsv
+ **filteredfasta(_i1, _i2 or _i3).tsv** - genomes that have all three genes within a group (i.e. nifHDK) from topfasta.tsv
+ **filt_wSSU_i3.tsv** - filteredhits_i3.tsv with SSU results from barrnap integrated
+ **NFixDB.tsv** - all results from iteration 3 compiled together
+ **RAW_Buckley_hits.tsv** - results from running our HMMs on Buckley's nifH database
+ **RAW_FunGene_hits.tsv** - results from running our HMMs on FunGene's nifH, nifD, and vnfD database
+ **RAW_Mise_hits.tsv** - results from running our HMMs on Mise's nifH database
+ **RAW_OutsideDBs_class.tsv** - results from running our HMMs on all outside databases
+ **RAW_OutsideDBs_hits.tsv** - filtered results from running our HMMs on all outside databases
+ **RAW_Zehr_hits.tsv** - results from running our HMMs on Zehr's nifH database
+ **topfasta(_i1, _i2 or _i3).tsv** - top results of each gene from evalue_taxonomy.tsv that are within cutoff of ≤ e-15 or bitscore of ≥ 50 
+ **tophits(_i1, _i2 or _i3).tsv** - top results of each gene from evalue_taxonomy.tsv. Gzipped due to large size

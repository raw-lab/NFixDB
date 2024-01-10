# Scripts

+ **aligns_hmms.sh** - MAFFT alignments and HMM builds for all files (i2-3)

+ **analysis.py** - runs analysis on tophits.tsv, finds which genomes have all three of each group of genes, outputs ***filteredhits.tsv***

+ **analysis_fasta.py** - same as analysis.py, but runs on topfasta.tsv, outputs ***filteredfasta.tsv***

+ **cd-hit.sh** - runs CD-HIT on fasta files to find clusters at 97%, 99%, and 100% similarity

+ **final.py** - makes/formats final TSV, outputs ***NFixDB.tsv***

+ **hmmsearch.sh** - combine HMMs and run hmmsearch

+ **nitrogenase_fastas.py** - creates new fasta files from ***filteredfasta.tsv***

+ **oDB_class.py** - same as taxonomy.py, but with an addiional cutoff of alignment length > 150 for the outside database results. Outputs ***oDB_class.tsv***

+ **oDB_cluster.sh** - clusters outside databases at 97%, 99%, and 100% similarity

+ **oDB_hits.py** - similar to tophits.py, find the top result of each sequence ID and outputs ***oDB_hits.tsv***

+ **oDB_hmm.sh** - runs hmmsearch on outside databases using the HMMs produced from i2-3

+ **sword_alns.sh** - runs SWORD on outside databases

+ **sword_[db].py** - analyzes SWORD results for corresponding database

+ **sql.py** - creates SQL database of all TSVs

+ **ssu.sh** - runs barrnap on genomes in filteredhits_i2-3.tsv

+ **ssu.py** - integrates SSU results into filteredhits_i2-3.tsv. Outputs ***filteredhits_SSU_i2-3.tsv***

+ **taxonomy.py** - finds sequences that are within ≤e-10 cutoff and gets taxonomy of genomes. Outputs ***evalue_taxonomy.tsv*** for those within cutoff range and ***oor_taxonomy.tsv*** for those out of the cutoff range

+ **topfastas.py** - same as tophits.py, but includes a cutoff of ≤e-15, bitscore of ≥50, or alignment length of >125. Outputs ***topfasta.tsv***

+ **tophits.py** - finds top results of each gene and sequence ID within the genomes (i.e. take the nifD result with e-104 rather than those with e-92 or e-63). Outputs ***tophits.tsv***

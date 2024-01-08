# Scripts

+ **alignments.sh** - MAFFT alignments and HMM builds for all files

+ **analysis.py** - runs analysis on tophits.tsv, finds which genomes have all three of each group of genes, outputs ***filteredhits.tsv***

+ **analysis_fasta.py** - same as analysis.py, but runs on topfasta.tsv, outputs ***filteredfasta.tsv***

+ **cd-hit.sh** - runs CD-HIT on fasta files to find clusters at 97%, 99%, and 100% similarity

+ **final.py** - makes/formats final TSV, outputs ***NFixDB.tsv***

+ **hmmsearch.sh** - combine HMMs and run hmmsearch

+ **nitrogenase_fastas.py** - creates new fasta files from ***filteredfasta.tsv***

+ **outsideDBs_class.sh** - runs outside_dbs_class.py and outside_dbs_hits.py

+ **outside_dbs.sh** - HMM searches of all outside databases analyzed

+ **outside_dbs_class.py** - same as taxonomy.py, but with outside databases results. Outputs ***RAW_OutsideDBs_class.tsv***

+ **outside_dbs_hits.py** - similar to tophits.py, find the top result of each sequence ID and outputs ***RAW_OutsideDBs_hits.tsv***

+ **sql.py** - creates SQL database of all TSVs

+ **ssu.sh** - runs barrnap on genomes in filteredhits_i3.tsv

+ **SSU_int.py** - integrates SSU results into filteredhits_i3.tsv. Outputs ***filt_wSSU_i3.tsv***

+ **tax_hits.sh** - runs taxonomy.py, tophits.py, topfastas.py, analysis.py, and nitrogenase_fastas.py

+ **taxonomy.py** - finds sequences that are within ≤ e-10 cutoff and gets taxonomy of genomes. Outputs ***evalue_taxonomy.tsv*** for those within cutoff range

+ **topfastas.py** - same as tophits.py, but includes a cutoff of ≤ e-15 or bitscore of ≥50. Outputs ***topfasta.tsv***

+ **tophits.py** - finds top results of each gene and sequence ID within the genomes (i.e. take the nifD result with e-104 rather than those with e-92 or e-63). Outputs ***tophits.tsv***

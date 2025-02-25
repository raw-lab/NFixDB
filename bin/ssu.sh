#!/bin/bash

INPUT=$1
OUTPATH=$2

# rsync -a /projects/raw_lab/databases/GTDB/protein_fna_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_fna_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined

mkdir -p results/SSUs

genomes=$(cut -f1 $INPUT) #column with genome IDs (GB_GCA_018902765.1)

#module load anaconda3
#conda activate barrnap 

echo "Running barrnap..."
#TODO: Should we differentiate bacteria from archaea in barrnap?
echo "Running barrnap on Genomes in GTDB" > barrnap-filter.log
for g in $genomes
do
    cat $GTDB_FNA/"$g"_protein.fna | barrnap -o $OUTPATH/"$g".faa --threads $SLURM_CPUS_ON_NODE &>>log-barrnap-filter.log
done

echo "Done"


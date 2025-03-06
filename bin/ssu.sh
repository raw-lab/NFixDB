#!/bin/bash

INPUT=$1
OUTPATH=$2

# rsync -a /projects/raw_lab/databases/GTDB/protein_fna_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_fna_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined

mkdir -p results/SSUs

genomes=$(cut -f1 $INPUT) #column with genome IDs (GB_GCA_018902765.1)

echo "Running barrnap..."
#TODO: Should we differentiate bacteria from archaea in barrnap?
echo "Running barrnap on Genomes in GTDB"
for g in $genomes
do
    if  [ -f $GTDB_FNA/archaea/"$g"_protein.fna.gz ] ; then
    	echo ARCHAEA "$g" >barrnap.log
        zcat $GTDB_FNA/archaea/"$g"_protein.fna.gz | barrnap -o $OUTPATH/"$g".faa --kingdom arc --threads $SLURM_CPUS_ON_NODE
    elif [ -f $GTDB_FNA/bacteria/"$g"_protein.fna.gz ] ; then
         zcat $GTDB_FNA/bacteria/"$g"_protein.fna.gz | barrnap -o $OUTPATH/"$g".faa --kingdom bac --threads $SLURM_CPUS_ON_NODE
    fi
done

echo "Done"


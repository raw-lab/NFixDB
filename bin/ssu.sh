#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-ssu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128GB
#SBATCH --time=5-0
#SBATCH -o slurm-%x-%j.out
#SBATCH --mail-type=END,FAIL,REQUEUE

echo "====================================================="
echo "Start Time  : $(date)"
echo "Submit Dir  : $SLURM_SUBMIT_DIR"
echo "Job ID/Name : $SLURM_JOBID / $SLURM_JOB_NAME"
echo "Node List   : $SLURM_JOB_NODELIST"
echo "Num Tasks   : $SLURM_NTASKS total [$SLURM_NNODES nodes @ $SLURM_CPUS_ON_NODE CPUs/node]"
echo "======================================================"
echo ""

#rsync -a /projects/raw_lab/databases/GTDB/protein_fna_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_fna_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined

mkdir -p SSUs

genomes=$(cut -f2 TSVs/filteredhits_i3.tsv) #column with genome IDs (GB_GCA_018902765.1)

for g in $genomes
do
    zcat /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined/"$g"_protein.fna.gz | barrnap -o ./SSUs/"$g".faa
done

python3 SSU_int.py

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


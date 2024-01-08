#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-combine
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

#rsync -av /projects/raw_lab/databases/GTDB/protein_faa_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_faa_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_faa_reps_r214-combined

for file in /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined/*; do 
        gunzip "$file" 
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


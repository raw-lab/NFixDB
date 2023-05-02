#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-len
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

#mkdir -p lengths 

#for file in /projects/raw_lab/databases/GTDB/protein_faa_reps_r207-combined/*; do
#    f="${file##*/}";
#    bioawk -c fastx '{ print $name, length($seq) }' < "$file" > lengths/${f%.faa}_length.out
#done

python3 lengths.py

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

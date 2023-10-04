#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=cd-hit
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
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

for file in fastas/i2/*; do
    cd-hit -i "$file" -o "${file%.faa}_100" -c 1.00
    cd-hit -i "$file" -o "${file%.faa}_99" -c 0.99
    cd-hit -i "$file" -o "${file%.faa}_97" -c 0.97
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

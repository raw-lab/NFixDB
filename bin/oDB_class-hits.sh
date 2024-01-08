#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=oDB-class-hits
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=128GB
#SBATCH --time=1-0
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

echo "Running oDB_class.py..."
python3 scripts/oDB_class.py
echo "Done"

echo "Running oDB_hits.py..."
python3 scripts/oDB_hits.py

echo "All Done"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

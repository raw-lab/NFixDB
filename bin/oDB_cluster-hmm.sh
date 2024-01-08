#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=oDB-Chmm
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

#HMM search
echo "Running hmmsearch on clustered oDBs"

for file in clusters/R2/oDB/*
do 
        hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 "$file" > "./oDB_results/clusters/$(basename -- $file)_anf_nif_vnf.out"
        hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 "$file" > "./oDB_results/clusters/$(basename -- $file)_nfl_chl.out"
done

echo "All Done"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""
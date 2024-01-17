#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=hmm
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=128GB
#SBATCH --time=2-0
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

#Combine anf/nif/vnf HMMs
cat ./HMMs/R2/i2-3/anfD-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/anfH-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/anfK-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/nifD-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/nifH-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/nifK-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/vnfD-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/vnfH-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/vnfK-local_i2-1_12182023.hmm > ./HMMs/R2/i2-3/anf_nif_vnf_i2-1_12182023

#Combine nfl/chl HMMs
cat ./HMMs/R2/i2-3/nflD-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/nflH-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/ChlN-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/ChIl-local_i2-1_12182023.hmm ./HMMs/R2/i2-3/ChlB-local_i2-1_12182023.hmm > ./HMMs/R2/i2-3/nfl_chl_i2-1_12182023

#HMM search
for file in /projects/raw_lab/databases/GTDB/protein_faa_reps_r214-combined/*; do 
        f="${file##*/}"
        hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-1_12182023 "$file" > "./bac120_ar53_results_i2-3/${f%.faa}_anf_nif_vnf.out"
        hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-1_12182023 "$file" > "./bac120_ar53_results_i2-3/${f%.faa}_nfl_chl.out"
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


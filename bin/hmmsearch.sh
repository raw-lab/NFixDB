#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-hmm
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

#Combine anf/nif/vnf HMMs
cat ./HMMs/new_anfD-local.hmm ./HMMs/new_anfH-local.hmm ./HMMs/new_anfK-local.hmm ./HMMs/new_nifD-local.hmm ./HMMs/new_nifH-local.hmm ./HMMs/new_nifK-local.hmm ./HMMs/new_vnfD-local.hmm ./HMMs/new_vnfH-local.hmm ./HMMs/new_vnfK-local.hmm > ./HMMs/anf_nif_vnf_i3

#Combine nfl/chl HMMs
cat ./HMMs/new_nflD-local.hmm ./HMMs/new_nflH-local.hmm ./HMMs/new_ChlN-local.hmm ./HMMs/new_ChIl-local.hmm ./HMMs/new_ChlB-local.hmm > ./HMMs/nfl_chl_i3

mkdir -p bac120_ar53_results_i3

#HMM search
for file in /projects/raw_lab/databases/GTDB/protein_faa_reps_r207-combined/*; do 
        f="${file##*/}"; 
        hmmsearch ./HMMs/anf_nif_vnf_i3 "$file" > "./bac120_ar53_results_i3/${f%.faa}_anf_nif_vnf.out";
        hmmsearch ./HMMs/nfl_chl_i3 "$file" > "./bac120_ar53_results_i3/${f%.faa}_nfl_chl.out";
done

conda deactivate

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


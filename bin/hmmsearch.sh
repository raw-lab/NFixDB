#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-hmm
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

#Combine anf/nif/vnf HMMs
cat ./HMMs/anfD-local_i3_08212023.hmm ./HMMs/anfH-local_i3_08212023.hmm ./HMMs/anfK-local_i3_08212023.hmm ./HMMs/nifD-local_i3_08212023.hmm ./HMMs/nifH-local_i3_08212023.hmm ./HMMs/nifK-local_i3_08212023.hmm ./HMMs/vnfD-local_i3_08212023.hmm ./HMMs/vnfH-local_i3_08212023.hmm ./HMMs/vnfK-local_i3_08212023.hmm > ./HMMs/anf_nif_vnf_i3_08282023

#Combine nfl/chl HMMs
cat ./HMMs/nflD-local_i3_08212023.hmm ./HMMs/nflH-local_i3_08212023.hmm ./HMMs/ChlN-local_i3_08212023.hmm ./HMMs/ChIl-local_i3_08212023.hmm ./HMMs/ChlB-local_i3_08212023.hmm > ./HMMs/nfl_chl_i3_08282023

#HMM search
for file in /projects/raw_lab/databases/GTDB/protein_faa_reps_r214-combined/*; do 
        f="${file##*/}"; 
        hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 "$file" > "./bac120_ar53_results_i3/${f%.faa}_anf_nif_vnf.out";
        hmmsearch ./HMMs/nfl_chl_i3_08282023 "$file" > "./bac120_ar53_results_i3/${f%.faa}_nfl_chl.out";
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


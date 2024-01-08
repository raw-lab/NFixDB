#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=oDB-hmm
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

#Buckley
echo "Running Buckley hmmsearch..."

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa > "./oDB_results/RAW_anf_nif_vnf_Buckley.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa > "./oDB_results/RAW_nfl_chl_Buckley.out"

echo "Done"

#FunGene
echo "Running FunGene hmmsearch..."

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/FunGene/FunGene_nifD-seeds.faa > "./oDB_results/RAW_anf_nif_vnf_FunGene-nifD.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/FunGene/FunGene_nifD-seeds.faa > "./oDB_results/RAW_nfl_chl_FunGene-nifD.out"

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/FunGene/FunGene_nifH-seeds.faa > "./oDB_results/RAW_anf_nif_vnf_FunGene-nifH.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/FunGene/FunGene_nifH-seeds.faa > "./oDB_results/RAW_nfl_chl_FunGene-nifH.out"

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/FunGene/FunGene_vnfD-seeds.faa > "./oDB_results/RAW_anf_nif_vnf_FunGene-vnfD.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/FunGene/FunGene_vnfD-seeds.faa > "./oDB_results/RAW_nfl_chl_FunGene-vnfD.out"

echo "Done"

#Mise
echo "Running Mise hmmsearch..."

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa > "./oDB_results/RAW_anf_nif_vnf_Mise-T1.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa > "./oDB_results/RAW_nfl_chl_Mise-T1.out"

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa > "./oDB_results/RAW_anf_nif_vnf_Mise-T2.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa > "./oDB_results/RAW_nfl_chl_Mise-T2.out"

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa > "./oDB_results/RAW_anf_nif_vnf_Mise-T3.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa > "./oDB_results/RAW_nfl_chl_Mise-T3.out"

echo "Done"

#Zehr
echo "Running Zehr hmmsearch..."

hmmsearch ./HMMs/R2/i2-3/anf_nif_vnf_i2-3_12222023 ../outside_dbs/Zehr/ZehrDB_nifH_prod.faa > "./oDB_results/RAW_anf_nif_vnf_Zehr.out" 
hmmsearch ./HMMs/R2/i2-3/nfl_chl_i2-3_12222023 ../outside_dbs/Zehr/ZehrDB_nifH_prod.faa > "./oDB_results/RAW_nfl_chl_Zehr.out"

echo "All Done"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

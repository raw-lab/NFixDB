#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=DBs
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

#Buckley
hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa > "RAW_anf_nif_vnf_Buckley.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa > "RAW_nfl_chl_Buckley.out";

#FunGene
hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/FunGene/FunGene_nifD-seeds.faa > "RAW_anf_nif_vnf_FunGene-nifD.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/FunGene/FunGene_nifD-seeds.faa > "RAW_nfl_chl_FunGene-nifD.out";

hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/FunGene/FunGene_nifH-seeds.faa > "RAW_anf_nif_vnf_FunGene-nifH.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/FunGene/FunGene_nifH-seeds.faa > "RAW_nfl_chl_FunGene-nifH.out";

hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/FunGene/FunGene_vnfD-seeds.faa > "RAW_anf_nif_vnf_FunGene-vnfD.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/FunGene/FunGene_vnfD-seeds.faa > "RAW_nfl_chl_FunGene-vnfD.out";

#Mise
hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa > "RAW_anf_nif_vnf_Mise-T1.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa > "RAW_nfl_chl_Mise-T1.out";

hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa > "RAW_anf_nif_vnf_Mise-T2.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa > "RAW_nfl_chl_Mise-T2.out";

hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa > "RAW_anf_nif_vnf_Mise-T3.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa > "RAW_nfl_chl_Mise-T3.out";

#Zehr
hmmsearch ./HMMs/anf_nif_vnf_i3_08282023 ../outside_dbs/Zehr/ZehrDB_nifH_prod.faa > "RAW_anf_nif_vnf_Zehr.out"; 
hmmsearch ./HMMs/nfl_chl_i3_08282023 ../outside_dbs/Zehr/ZehrDB_nifH_prod.faa > "RAW_nfl_chl_Zehr.out";

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

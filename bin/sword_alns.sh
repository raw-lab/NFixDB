#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=sword-nifH
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
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

module load anaconda3
conda activate sword

# Buckley
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/Buckley_nifH_97 -A NW -o sword/nifH-Buckley_nifH_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/Buckley_nifH_97 -A NW -o sword/anfH-Buckley_nifH_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/Buckley_nifH_97 -A NW -o sword/vnfH-Buckley_nifH_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/Buckley_nifH_97 -A NW -o sword/nflH-Buckley_nifH_97.out

# FunGene - nifH
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/FunGene_nifH_97 -A NW -o sword/nifH-FunGene_nifH_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/FunGene_nifH_97 -A NW -o sword/anfH-FunGene_nifH_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/FunGene_nifH_97 -A NW -o sword/vnfH-FunGene_nifH_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/FunGene_nifH_97 -A NW -o sword/nflH-FunGene_nifH_97.out

# Mise - T1
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T1_97 -A NW -o sword/nifH-Mise_nifH_T1_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T1_97 -A NW -o sword/anfH-Mise_nifH_T1_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T1_97 -A NW -o sword/vnfH-Mise_nifH_T1_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T1_97 -A NW -o sword/nflH-Mise_nifH_T1_97.out

# Mise - T2
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T2_97 -A NW -o sword/nifH-Mise_nifH_T2_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T2_97 -A NW -o sword/anfH-Mise_nifH_T2_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T2_97 -A NW -o sword/vnfH-Mise_nifH_T2_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T2_97 -A NW -o sword/nflH-Mise_nifH_T2_97.out

# Mise - T3
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T3_97 -A NW -o sword/nifH-Mise_nifH_T3_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T3_97 -A NW -o sword/anfH-Mise_nifH_T3_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T3_97 -A NW -o sword/vnfH-Mise_nifH_T3_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/Mise_nifH_T3_97 -A NW -o sword/nflH-Mise_nifH_T3_97.out

# Zehr
sword -i fastas/R2/final/nifH_01032024.faa -j clusters/R2/oDB/97/faa/Zehr_nifH_97 -A NW -o sword/nifH-Zehr_nifH_97.out
sword -i fastas/R2/final/anfH_01032024.faa -j clusters/R2/oDB/97/faa/Zehr_nifH_97 -A NW -o sword/anfH-Zehr_nifH_97.out
sword -i fastas/R2/final/vnfH_01032024.faa -j clusters/R2/oDB/97/faa/Zehr_nifH_97 -A NW -o sword/vnfH-Zehr_nifH_97.out
sword -i fastas/R2/final/nflH_01032024.faa -j clusters/R2/oDB/97/faa/Zehr_nifH_97 -A NW -o sword/nflH-Zehr_nifH_97.out

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""
#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=sword-all
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

for file in fastas/R2/i2-2/*
do
    f="${file##*/}"
    f="${f%%_*}"

    # Buckley
    sword -i clusters/R2/oDB/97/faa/Buckley_nifH_97 -j $file -A NW -o sword/i2/Buckley/$f-Buckley_nifH_97.out

    # FunGene
    sword -i clusters/R2/oDB/97/faa/FunGene_nifH_97 -j $file -A NW -o sword/i2/FunGene/$f-FunGene_nifH_97.out
    sword -i clusters/R2/oDB/97/faa/FunGene_nifD_97 -j $file -A NW -o sword/i2/FunGene/$f-FunGene_nifD_97.out
    sword -i clusters/R2/oDB/97/faa/FunGene_vnfD_97 -j $file -A NW -o sword/i2/FunGene/$f-FunGene_vnfD_97.out

    # Mise
    sword -i clusters/R2/oDB/97/faa/Mise_nifH_T1_97 -j $file -A NW -o sword/i2/Mise/$f-MiseT1_nifH_97.out
    sword -i clusters/R2/oDB/97/faa/Mise_nifH_T2_97 -j $file -A NW -o sword/i2/Mise/$f-MiseT2_nifH_97.out
    sword -i clusters/R2/oDB/97/faa/Mise_nifH_T3_97 -j $file -A NW -o sword/i2/Mise/$f-MiseT3_nifH_97.out

    # Zehr
    sword -i clusters/R2/oDB/97/faa/Zehr_nifH_97 -j $file -A NW -o sword/i2/Zehr/$f-Zehr_nifH_97.out
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""
#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-Workflow
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB
#SBATCH --time=0-10
#SBATCH -o slurm-%x-%j.out
#SBATCH --mail-type=END,FAIL,REQUEUE

#############
# README
# 
# Requirements:
# mafft
# hmmer
# barrnap
# biopython
# pandas
# 
# Description:
# This SLURM script runs every step of the 
# NFixDB workflow on a cluster environment.
# 
# Running:
# command: sbatch nfixdb-workflow.sh
# The SBATCH settings above will need to be
# modified for your environment.
# The dependencies will need to be loaded through
# a server module or an Anaconda environment
# 


echo "====================================================="
echo "Start Time  : $(date)"
echo "Submit Dir  : $SLURM_SUBMIT_DIR"
echo "Job ID/Name : $SLURM_JOBID / $SLURM_JOB_NAME"
echo "Node List   : $SLURM_JOB_NODELIST"
echo "Num Tasks   : $SLURM_NTASKS total [$SLURM_NNODES nodes @ $SLURM_CPUS_ON_NODE CPUs/node With $SLURM_CPUS_PER_TASK CPUs/task]"
echo "======================================================"
echo ""

SECONDS=0

module load anaconda3
eval "$(conda shell.bash hook)"
conda activate NFixDB

CPUS=$SLURM_CPUS_PER_TASK

GTDB_PATH="/projects/raw_lab/databases/GTDB/protein_faa_reps_r214-combined"

SEEDS="data/seeds/initial"
RESULTS=results/i1
ALIGN_DIR=$RESULTS/alignments
HMM_DIR=$RESULTS/HMMs
OUTDIR=$RESULTS/bac120_ar53
OUTTSV=$RESULTS/TSVs
OUTFASTA=$RESULTS/fastas
OUTSSU=$RESULTS/SSUs

mkdir -p $ALIGN_DIR
mkdir -p $HMM_DIR
mkdir -p $OUTDIR
mkdir -p $OUTTSV
mkdir -p $OUTFASTA
mkdir -p $OUTSSU


#echo "======================================================"
#echo "Aligning fastas and creating HMMs   : $(date)"
#echo "======================================================"
#command time bash bin/aligns_hmms.sh $SEEDS $ALIGN_DIR $HMM_DIR $CPUS >log01-align.txt
#
#echo "======================================================"
#echo "hmmsearch   : $(date)"
#echo "======================================================"
#command time bash bin/hmmsearch.sh $HMM_DIR $OUTDIR $GTDB_PATH $CPUS >log02-hmmsearch.txt
#
echo "======================================================"
echo "Taxonomy   : $(date)"
echo "======================================================"
command time python bin/taxonomy.py --hitpath $OUTDIR --outfile $OUTTSV/evalue_taxonomy.tsv  >log03-taxonomy.txt

echo "======================================================"
echo "Top hits   : $(date)"
echo "======================================================"
command time python bin/tophits.py -i $OUTTSV/evalue_taxonomy.tsv -o $OUTTSV >log04-top_hits.txt

#echo "======================================================"
#echo "Top hit analysis   : $(date)"
#echo "======================================================"
#command time python bin/analysis.py
#
#echo "======================================================"
#echo "Top fastas analysis   : $(date)"
#echo "======================================================"
#command time python bin/analysis_fasta.py
#
#echo "======================================================"
#echo "Nitrogenase   : $(date)"
#echo "======================================================"
#command time python bin/nitrogenase_fastas.py
#
#echo "======================================================"
#echo "SSU   : $(date)"
#echo "======================================================"
#command time bash bin/ssu.sh
#
#echo "======================================================"
#echo "Final TSV   : $(date)"
#echo "======================================================"
#command time python bin/final.py
#
#echo "======================================================"
#echo "Create final SQL   : $(date)"
#echo "======================================================"
#command time python bin/sql.py
#
#
#echo "======================================================"
#echo "NFixDB ITERATION 2   : $(date)"
#echo "======================================================"
#
#SEEDS="$RESULTS/fastas"
#RESULTS=results/i2
#ALIGN_DIR=$RESULTS/alignments
#HMM_DIR=$RESULTS/HMMs
#OUTDIR=$RESULTS/bac120_ar53
#
#mkdir -p $ALIGN_DIR
#mkdir -p $HMM_DIR
#mkdir -p $OUTDIR
#mkdir -p $OUTTSV
#mkdir -p $OUTFASTA
#mkdir -p $OUTSSU
#
#
#echo "======================================================"
#echo "Aligning new fastas and creating HMMs   : $(date)"
#echo "======================================================"
#command time bash bin/aligns_hmms.sh
#
#echo "======================================================"
#echo "hmmsearch new hmms   : $(date)"
#echo "======================================================"
#command time bash bin/hmmsearch.sh


echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "Run Time   : $SECONDS"
echo "======================================================"
echo ""


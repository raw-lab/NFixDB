#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-Workflow
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=0
#SBATCH --time=5-0
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
# a server module or an Anaconda environment.
# 
# Before running, make sure that the GTDB_PATH
# and GTDB_FNA point to a valid path containing
# the protein and nucleotide, reference files from
# GTDB, respectively.

if [ -z "$SLURM_CPUS_ON_NODE" ]
then
	SLURM_JOBID=NFixDB-Workflow
	SLURM_JOB_NODELIST=$(hostname)
	SLURM_NTASKS=1
	SLURM_NNODES=1
	SLURM_CPUS_ON_NODE=1
	SLURM_CPUS_PER_TASK=1
	SLURM_SUBMIT_DIR=$(pwd)
	SLURM_JOBID=0
fi

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

export GTDB_PATH="/projects/raw_lab/databases/GTDB/v220/protein_faa_reps"
export GTDB_FNA="/projects/raw_lab/databases/GTDB/v220/protein_fna_reps"


SEEDS="data/seeds/initial"
RESULTS=results/i1
ALIGN_DIR=$RESULTS/alignments
HMM_DIR=$RESULTS/HMMs
OUTDIR=$RESULTS/bac120_ar53
OUTTSV=$RESULTS/TSVs
OUTFASTA=$RESULTS/fastas
OUTSSU=$RESULTS/SSUs
LOG=$RESULTS/log

mkdir -p $ALIGN_DIR
mkdir -p $HMM_DIR
mkdir -p $OUTDIR
mkdir -p $OUTTSV
mkdir -p $OUTFASTA
mkdir -p $OUTSSU
mkdir -p $LOG


echo "======================================================"
echo "Aligning fastas and creating HMMs"
echo "$(date)"
echo "======================================================"
time (command time bash bin/aligns_hmms.sh $SEEDS $ALIGN_DIR $HMM_DIR $CPUS &>$LOG/01-align.txt)

echo "======================================================"
echo "hmmsearch"
echo "$(date)"
echo "======================================================"
time (command time bash bin/hmmsearch.sh $HMM_DIR $OUTDIR $GTDB_PATH $CPUS &>$LOG/02-hmmsearch.txt)

echo "======================================================"
echo "Taxonomy"
echo "$(date)"
echo "======================================================"
command time python bin/taxonomy.py --hitpath $OUTDIR --outfile $OUTTSV/evalue_taxonomy.tsv  >$LOG/03-taxonomy.txt

echo "======================================================"
echo "Top hits"
echo "$(date)"
echo "======================================================"
command time python bin/tophits.py -i $OUTTSV/evalue_taxonomy.tsv -o $OUTTSV >$LOG/04-top_hits.txt

echo "======================================================"
echo "Top hit analysis"
echo "$(date)"
echo "======================================================"
command time python bin/analysis.py --input $OUTTSV/tophits.tsv --output $OUTTSV/filteredhits.tsv >$LOG/05-hit_analysis.txt

echo "======================================================"
echo "Top fastas analysis"
echo "$(date)"
echo "======================================================"
command time python bin/analysis_fasta.py --input $OUTTSV/topfasta.tsv --output $OUTTSV/filteredfasta.tsv >$LOG/06-fasta_analysis.txt

echo "======================================================"
echo "Nitrogenase"
echo "$(date)"
echo "======================================================"
command time python bin/nitrogenase_fastas.py --input $OUTTSV/filteredfasta.tsv --output $OUTFASTA --gtdb $GTDB_PATH >$LOG/07-nitrogenase.txt

echo "======================================================"
echo "SSU"
echo "$(date)"
echo "======================================================"
command time bash bin/ssu.sh $OUTTSV/filteredhits.tsv $OUTSSU &>$LOG/07-ssu.txt
echo "Running ssu.py..."
command time python3 bin/ssu.py --input $OUTTSV/filteredhits.tsv --output $OUTTSV/filteredhits_SSU.tsv --ssu $OUTSSU >$LOG/08-ssu.txt
echo "SSU all Done"

echo "======================================================"
echo "Final TSV"
echo "$(date)"
echo "======================================================"
command time python bin/final.py --input $OUTTSV/filteredhits_SSU.tsv --output $OUTTSV/NFixDB.tsv >$LOG/09-final.txt

echo "======================================================"
echo "Create final SQL"
echo "$(date)"
echo "======================================================"
command time python bin/sql.py --input $OUTTSV --output $OUTTSV/NFixDB.db >$LOG/10-final_sql.txt


echo
echo "======================================================"
echo
echo "NFixDB ITERATION 2   : $(date)"
echo
echo "======================================================"
echo

SEEDS="$RESULTS/fastas"
RESULTS=results/i2
ALIGN_DIR=$RESULTS/alignments
HMM_DIR=$RESULTS/HMMs
OUTDIR=$RESULTS/bac120_ar53
OUTTSV=$RESULTS/TSVs
OUTFASTA=$RESULTS/fastas
OUTSSU=$RESULTS/SSUs
LOG=$RESULTS/log


mkdir -p $ALIGN_DIR
mkdir -p $HMM_DIR
mkdir -p $OUTDIR
mkdir -p $OUTTSV
mkdir -p $OUTFASTA
mkdir -p $OUTSSU
mkdir -p $LOG


echo "======================================================"
echo "Aligning fastas and creating HMMs"
echo "$(date)"
echo "======================================================"
time (command time bash bin/aligns_hmms.sh $SEEDS $ALIGN_DIR $HMM_DIR $CPUS &>$LOG/01-align.txt)

echo "======================================================"
echo "hmmsearch"
echo "$(date)"
echo "======================================================"
time (command time bash bin/hmmsearch.sh $HMM_DIR $OUTDIR $GTDB_PATH $CPUS &>$LOG/02-hmmsearch.txt)

echo "======================================================"
echo "Taxonomy"
echo "$(date)"
echo "======================================================"
command time python bin/taxonomy.py --hitpath $OUTDIR --outfile $OUTTSV/evalue_taxonomy.tsv  >$LOG/03-taxonomy.txt

echo "======================================================"
echo "Top hits"
echo "$(date)"
echo "======================================================"
command time python bin/tophits.py -i $OUTTSV/evalue_taxonomy.tsv -o $OUTTSV >$LOG/04-top_hits.txt

echo "======================================================"
echo "Top hit analysis"
echo "$(date)"
echo "======================================================"
command time python bin/analysis.py --input $OUTTSV/tophits.tsv --output $OUTTSV/filteredhits.tsv >$LOG/05-hit_analysis.txt

echo "======================================================"
echo "Top fastas analysis"
echo "$(date)"
echo "======================================================"
command time python bin/analysis_fasta.py --input $OUTTSV/topfasta.tsv --output $OUTTSV/filteredfasta.tsv >$LOG/06-fasta_analysis.txt

echo "======================================================"
echo "Nitrogenase"
echo "$(date)"
echo "======================================================"
command time python bin/nitrogenase_fastas.py --input $OUTTSV/filteredfasta.tsv --output $OUTFASTA --gtdb $GTDB_PATH >$LOG/07-nitrogenase.txt

echo "======================================================"
echo "SSU"
echo "$(date)"
echo "======================================================"
command time bash bin/ssu.sh $OUTTSV/filteredhits.tsv $OUTSSU &>$LOG/07-ssu.txt
echo "Running ssu.py..."
command time python3 bin/ssu.py --input $OUTTSV/filteredhits.tsv --output $OUTTSV/filteredhits_SSU.tsv --ssu $OUTSSU >$LOG/08-ssu.txt
echo "SSU all Done"

echo "======================================================"
echo "Final TSV"
echo "$(date)"
echo "======================================================"
command time python bin/final.py --input $OUTTSV/filteredhits_SSU.tsv --output $OUTTSV/NFixDB.tsv >$LOG/09-final.txt

echo "======================================================"
echo "Create final SQL"
echo "$(date)"
echo "======================================================"
command time python bin/sql.py --input $OUTTSV --output $OUTTSV/NFixDB.db >$LOG/10-final_sql.txt



echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "Run Time   : $SECONDS seconds"
echo "======================================================"
echo ""


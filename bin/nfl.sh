#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=nfl
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

mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nflD_12222023.faa > ../alignments/R2/i2-3/nflD-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nflH_12222023.faa > ../alignments/R2/i2-3/nflH-local_aln_i2-3_12222023.faa

hmmbuild ../HMMs/R2/i2-3/nflD-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nflD-local_aln_i2-3_12222023.faa
hmmbuild ../HMMs/R2/i2-3/nflH-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nflH-local_aln_i2-3_12222023.faa

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


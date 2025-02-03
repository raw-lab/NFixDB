#!/bin/bash

#SBATCH --partition=Draco
#SBATCH --job-name=NFixDB-align_build-hmms
#SBATCH --nodes=1
#SBATCH --cpus-per-task=36
#SBATCH --mem=376GB
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

CPUS=$SLURM_CPUS_ON_NODE

mkdir -p results/alignments/
mkdir -p results/HMMs/


#anf
echo "======================================================"
echo "Aligning anf   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/anfD_*.faa > results/alignments/anfD-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/anfH_*.faa > results/alignments/anfH-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/anfK_*.faa > results/alignments/anfK-gtdb.faa

echo "======================================================"
echo "Building anf HMMs   : $(date)"

hmmbuild --cpu $CPUS results/HMMs/anfD-gtdb_.hmm results/alignments/anfD-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/anfH-gtdb_.hmm results/alignments/anfH-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/anfK-gtdb_.hmm results/alignments/anfK-gtdb.faa

#nif
echo "======================================================"
echo "Aligning nif   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/nifH_*.faa > results/alignments/nifH-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/nifD_*.faa > results/alignments/nifD-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/nifK_*.faa > results/alignments/nifK-gtdb.faa

echo "======================================================"
echo "Building nif HMMs   : $(date)"

hmmbuild --cpu $CPUS results/HMMs/nifH-gtdb_.hmm results/alignments/nifH-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/nifD-gtdb_.hmm results/alignments/nifD-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/nifK-gtdb_.hmm results/alignments/nifK-gtdb.faa

#vnf
echo "======================================================"
echo "Aligning vnf   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/vnfD_*.faa > results/alignments/vnfD-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/vnfH_*.faa > results/alignments/vnfH-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/vnfK_*.faa > results/alignments/vnfK-gtdb.faa

echo "======================================================"
echo "Building vnf HMMs   : $(date)"

hmmbuild --cpu $CPUS results/HMMs/vnfD-gtdb_.hmm results/alignments/vnfD-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/vnfH-gtdb_.hmm results/alignments/vnfH-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/vnfK-gtdb_.hmm results/alignments/vnfK-gtdb.faa

#Chl
echo "======================================================"
echo "Aligning Chl   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/ChIl_*.faa > results/alignments/ChIl-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/ChlN-BchN_*.faa > results/alignments/ChlN-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/ChlB-BchB_*.faa > results/alignments/ChlB-gtdb.faa

echo "======================================================"
echo "Building chl HMMs   : $(date)"

hmmbuild --cpu $CPUS results/HMMs/ChIl-gtdb_.hmm results/alignments/ChIl-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/ChlN-gtdb_.hmm results/alignments/ChlN-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/ChlB-gtdb_.hmm results/alignments/ChlB-gtdb.faa

#nfl
echo "======================================================"
echo "Aligning nfl   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/nflD_*.faa > results/alignments/nflD-gtdb.faa
mafft --thread $CPUS --localpair --maxiterate 1000 results/fastas/nflH_*.faa > results/alignments/nflH-gtdb.faa

echo "======================================================"
echo "Building nfl HMMs   : $(date)"

hmmbuild --cpu $CPUS results/HMMs/nflD-gtdb_.hmm results/alignments/nflD-gtdb.faa
hmmbuild --cpu $CPUS results/HMMs/nflH-gtdb_.hmm results/alignments/nflH-gtdb.faa

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


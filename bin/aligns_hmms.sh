#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=all-alns-hmms
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
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

#anf
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/anfD_12222023.faa > ../alignments/R2/i2-3/anfD-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/anfH_12222023.faa > ../alignments/R2/i2-3/anfH-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/anfK_12222023.faa > ../alignments/R2/i2-3/anfK-local_aln_i2-3_12222023.faa

hmmbuild ./HMMs/anfD-local_i2-3_12222023.hmm ../alignments/R2/i2-3/anfD-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/anfH-local_i2-3_12222023.hmm ../alignments/R2/i2-3/anfH-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/anfK-local_i2-3_12222023.hmm ../alignments/R2/i2-3/anfK-local_aln_i2-3_12222023.faa

#nif
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nifH_12222023.faa > ../alignments/R2/i2-3/nifH-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nifD_12222023.faa > ../alignments/R2/i2-3/nifD-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nifK_12222023.faa > ../alignments/R2/i2-3/nifK-local_aln_i2-3_12222023.faa

hmmbuild ./HMMs/nifH-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nifH-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/nifD-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nifD-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/nifK-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nifK-local_aln_i2-3_12222023.faa

#vnf
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/vnfD_12222023.faa > ../alignments/R2/i2-3/vnfD-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/vnfH_12222023.faa > ../alignments/R2/i2-3/vnfH-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/vnfK_12222023.faa > ../alignments/R2/i2-3/vnfK-local_aln_i2-3_12222023.faa

hmmbuild ./HMMs/vnfD-local_i2-3_12222023.hmm ../alignments/R2/i2-3/vnfD-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/vnfH-local_i2-3_12222023.hmm ../alignments/R2/i2-3/vnfH-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/vnfK-local_i2-3_12222023.hmm ../alignments/R2/i2-3/vnfK-local_aln_i2-3_12222023.faa

#Chl
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/ChIl_12222023.faa > ../alignments/R2/i2-3/ChIl-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/ChlN-BchN_12222023.faa > ../alignments/R2/i2-3/ChlN-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/ChlB-BchB_12222023.faa > ../alignments/R2/i2-3/ChlB-local_aln_i2-3_12222023.faa

hmmbuild ./HMMs/ChIl-local_i2-3_12222023.hmm ../alignments/R2/i2-3/ChIl-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/ChlN-local_i2-3_12222023.hmm ../alignments/R2/i2-3/ChlN-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/ChlB-local_i2-3_12222023.hmm ../alignments/R2/i2-3/ChlB-local_aln_i2-3_12222023.faa

#nfl
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nflD_12222023.faa > ../alignments/R2/i2-3/nflD-local_aln_i2-3_12222023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/i2-3/nflH_12222023.faa > ../alignments/R2/i2-3/nflH-local_aln_i2-3_12222023.faa

hmmbuild ./HMMs/nflD-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nflD-local_aln_i2-3_12222023.faa
hmmbuild ./HMMs/nflH-local_i2-3_12222023.hmm ../alignments/R2/i2-3/nflH-local_aln_i2-3_12222023.faa

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


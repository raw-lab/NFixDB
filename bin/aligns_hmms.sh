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
mafft --localpair --maxiterate 1000 ../fastas/R2/final/anfD_12192023.faa > ../alignments/R2/final/anfD-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/anfH_12192023.faa > ../alignments/R2/final/anfH-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/anfK_12192023.faa > ../alignments/R2/final/anfK-local_aln_i2-2_12192023.faa

hmmbuild ./HMMs/anfD-local_final_12192023.hmm ../alignments/R2/final/anfD-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/anfH-local_final_12192023.hmm ../alignments/R2/final/anfH-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/anfK-local_final_12192023.hmm ../alignments/R2/final/anfK-local_aln_i2-2_12192023.faa

#nif
mafft --localpair --maxiterate 1000 ../fastas/R2/final/nifH_12192023.faa > ../alignments/R2/final/nifH-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/nifD_12192023.faa > ../alignments/R2/final/nifD-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/nifK_12192023.faa > ../alignments/R2/final/nifK-local_aln_i2-2_12192023.faa

hmmbuild ./HMMs/nifH-local_final_12192023.hmm ../alignments/R2/final/nifH-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/nifD-local_final_12192023.hmm ../alignments/R2/final/nifD-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/nifK-local_final_12192023.hmm ../alignments/R2/final/nifK-local_aln_i2-2_12192023.faa

#vnf
mafft --localpair --maxiterate 1000 ../fastas/R2/final/vnfD_12192023.faa > ../alignments/R2/final/vnfD-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/vnfH_12192023.faa > ../alignments/R2/final/vnfH-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/vnfK_12192023.faa > ../alignments/R2/final/vnfK-local_aln_i2-2_12192023.faa

hmmbuild ./HMMs/vnfD-local_final_12192023.hmm ../alignments/R2/final/vnfD-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/vnfH-local_final_12192023.hmm ../alignments/R2/final/vnfH-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/vnfK-local_final_12192023.hmm ../alignments/R2/final/vnfK-local_aln_i2-2_12192023.faa

#Chl
mafft --localpair --maxiterate 1000 ../fastas/R2/final/ChIl_12192023.faa > ../alignments/R2/final/ChIl-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/ChlN-BchN_12192023.faa > ../alignments/R2/final/ChlN-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/ChlB-BchB_12192023.faa > ../alignments/R2/final/ChlB-local_aln_i2-2_12192023.faa

hmmbuild ./HMMs/ChIl-local_final_12192023.hmm ../alignments/R2/final/ChIl-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/ChlN-local_final_12192023.hmm ../alignments/R2/final/ChlN-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/ChlB-local_final_12192023.hmm ../alignments/R2/final/ChlB-local_aln_i2-2_12192023.faa

#nfl
mafft --localpair --maxiterate 1000 ../fastas/R2/final/nflD_12192023.faa > ../alignments/R2/final/nflD-local_aln_i2-2_12192023.faa
mafft --localpair --maxiterate 1000 ../fastas/R2/final/nflH_12192023.faa > ../alignments/R2/final/nflH-local_aln_i2-2_12192023.faa

hmmbuild ./HMMs/nflD-local_final_12192023.hmm ../alignments/R2/final/nflD-local_aln_i2-2_12192023.faa
hmmbuild ./HMMs/nflH-local_final_12192023.hmm ../alignments/R2/final/nflH-local_aln_i2-2_12192023.faa

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


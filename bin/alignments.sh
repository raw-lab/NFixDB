#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-chl
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
mafft --localpair --maxiterate 1000 ./fastas/i3/anfD_08212023.faa > ./alignments/anfD-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i3/anfH_08212023.faa > ./alignments/anfH-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i3/anfK_08212023.faa > ./alignments/anfK-local_aln_i3_08212023.faa;

hmmbuild ./HMMs/anfD-local_i3_08212023.hmm ./alignments/anfD-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/anfH-local_i3_08212023.hmm ./alignments/anfH-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/anfK-local_i3_08212023.hmm ./alignments/anfK-local_aln_i3_08212023.faa;

#nif
mafft --localpair --maxiterate 1000 ./fastas/i3/nifH_08212023.faa > ./alignments/nifH-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i1/nifD_08082023.faa > ./alignments/nifD-local_aln_i1_08082023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i1/nifK_08082023.faa > ./alignments/nifK-local_aln_i1_08082023.faa;

hmmbuild ./HMMs/nifH-local_i3_08212023.hmm ./alignments/nifH-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/nifD-local_i1_08082023.hmm ./alignments/nifD-local_aln_i1_08082023.faa;
hmmbuild ./HMMs/nifK-local_i1_08082023.hmm ./alignments/nifK-local_aln_i1_08082023.faa;

#vnf
mafft --localpair --maxiterate 1000 ./fastas/i3/vnfD_08212023.faa > ./alignments/vnfD-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i3/vnfH_08212023.faa > ./alignments/vnfH-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i3/vnfK_08212023.faa > ./alignments/vnfK-local_aln_i3_08212023.faa;

hmmbuild ./HMMs/vnfD-local_i3_08212023.hmm ./alignments/vnfD-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/vnfH-local_i3_08212023.hmm ./alignments/vnfH-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/vnfK-local_i3_08212023.hmm ./alignments/vnfK-local_aln_i3_08212023.faa;

#Chl
mafft --localpair --maxiterate 1000 ./fastas/i3/ChIl_08212023.faa > ./alignments/ChIl-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i1/ChlN-BchN_08082023.faa > ./alignments/ChlN-local_aln_i1_08082023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i1/ChlB-BchB_08082023.faa > ./alignments/ChlB-local_aln_i1_08082023.faa;

hmmbuild ./HMMs/ChIl-local_i3_08212023.hmm ./alignments/ChIl-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/ChlN-local_i3_08212023.hmm ./alignments/ChlN-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/ChlB-local_i3_08212023.hmm ./alignments/ChlB-local_aln_i3_08212023.faa;

#nfl
mafft --localpair --maxiterate 1000 ./fastas/i3/nflD_08212023.faa > ./alignments/nflD-local_aln_i3_08212023.faa;
mafft --localpair --maxiterate 1000 ./fastas/i3/nflH_08212023.faa > ./alignments/nflH-local_aln_i3_08212023.faa;

hmmbuild ./HMMs/nflD-local_i3_08212023.hmm ./alignments/nflD-local_aln_i3_08212023.faa;
hmmbuild ./HMMs/nflH-local_i3_08212023.hmm ./alignments/nflH-local_aln_i3_08212023.faa;

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


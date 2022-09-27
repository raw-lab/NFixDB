#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
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

module load mafft
module load anaconda3
conda activate hmmer

#Run alignments on seed sequences
mafft --localpair --maxiterate 1000 ./fastas/new_anfD.faa > ./alignments/new_anfD-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_anfH.faa > ./alignments/new_anfH-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_anfK.faa > ./alignments/new_anfK-local_aln.faa;

mafft --localpair --maxiterate 1000 ./fastas/new_nifD.faa > ./alignments/new_nifD-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_nifH.faa > ./alignments/new_nifH-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_nifK.faa > ./alignments/new_nifK-local_aln.faa;

mafft --localpair --maxiterate 1000 ./fastas/new_vnfD.faa > ./alignments/new_vnfD-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_vnfH.faa > ./alignments/new_vnfH-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_vnfK.faa > ./alignments/new_vnfK-local_aln.faa;

mafft --localpair --maxiterate 1000 ./fastas/new_nflD.faa > ./alignments/new_nflD-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_nflH.faa > ./alignments/new_nflH-local_aln.faa;

mafft --localpair --maxiterate 1000 ./fastas/new_ChlB.faa > ./alignments/new_ChlB-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_ChlN.faa > ./alignments/new_ChlN-local_aln.faa;
mafft --localpair --maxiterate 1000 ./fastas/new_ChIl.faa > ./alignments/new_ChIl-local_aln.faa;

#Build HMMs
hmmbuild ./HMMs/new_anfD-local.hmm ./alignments/new_anfD-local_aln.faa;
hmmbuild ./HMMs/new_anfH-local.hmm ./alignments/new_anfH-local_aln.faa;
hmmbuild ./HMMs/new_anfK-local.hmm ./alignments/new_anfK-local_aln.faa;

hmmbuild ./HMMs/new_nifK-local.hmm ./alignments/new_nifK-local_aln.faa;
hmmbuild ./HMMs/new_nifK-local.hmm ./alignments/new_nifK-local_aln.faa;
hmmbuild ./HMMs/new_nifK-local.hmm ./alignments/new_nifK-local_aln.faa;

hmmbuild ./HMMs/new_vnfD-local.hmm ./alignments/new_vnfD-local_aln.faa;
hmmbuild ./HMMs/new_vnfH-local.hmm ./alignments/new_vnfH-local_aln.faa;
hmmbuild ./HMMs/new_vnfK-local.hmm ./alignments/new_vnfK-local_aln.faa;

hmmbuild ./HMMs/new_nflD-local.hmm ./alignments/new_nflD-local_aln.faa;
hmmbuild ./HMMs/new_nflH-local.hmm ./alignments/new_nflH-local_aln.faa;

hmmbuild ./HMMs/new_ChlB-local.hmm ./alignments/new_ChlB-local_aln.faa;
hmmbuild ./HMMs/new_ChlN-local.hmm ./alignments/new_ChlN-local_aln.faa;
hmmbuild ./HMMs/new_ChIl-local.hmm ./alignments/new_ChIl-local_aln.faa;

#Combine anf/nif/vnf HMMs
cat ./HMMs/new_anfD-local.hmm ./HMMs/new_anfH-local.hmm ./HMMs/new_anfK-local.hmm ./HMMs/new_nifD-local.hmm ./HMMs/new_nifH-local.hmm ./HMMs/new_nifK-local.hmm ./HMMs/new_vnfD-local.hmm ./HMMs/new_vnfH-local.hmm ./HMMs/new_vnfK-local.hmm > ./HMMs/anf_nif_vnf_i3

#Combine nfl/chl HMMs
cat ./HMMs/new_nflD-local.hmm ./HMMs/new_nflH-local.hmm ./HMMs/new_ChlN-local.hmm ./HMMs/new_ChIl-local.hmm ./HMMs/new_ChlB-local.hmm > ./HMMs/nfl_chl_i3

mkdir -p bac120_ar53_results_i3

#HMM search
for file in /projects/raw_lab/databases/GTDB/protein_faa_reps_r207-combined/*; do 
        f="${file##*/}"; 
        hmmsearch ./HMMs/anf_nif_vnf_i3 "$file" > "./bac120_ar53_results_i3/${f%.faa}_anf_nif_vnf.out";
        hmmsearch ./HMMs/nfl_chl_i3 "$file" > "./bac120_ar53_results_i3/${f%.faa}_nfl_chl.out";
done

conda deactivate

#Get full taxonomy
python3 taxonomy.py

#Find top hits
python3 tophits.py

#Find better top hits for fastas
python3 topfastas.py

#Filter the top hits for fastas
python3 analysis.py

#Remake fastas
python3 nitrogenase_fastas.py

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

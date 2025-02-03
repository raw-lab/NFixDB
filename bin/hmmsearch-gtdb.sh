#!/bin/bash

#SBATCH --partition=Draco
#SBATCH --job-name=NFixDB-hmmsearch
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=36
#SBATCH --mem=376GB
#SBATCH --time=2-0
#SBATCH -o slurm-%x-%j.out
#SBATCH --mail-type=END,FAIL,REQUEUE

echo "====================================================="
echo "Start Time  : $(date)"
echo "Submit Dir  : $SLURM_SUBMIT_DIR"
echo "Job ID/Name : $SLURM_JOBID / $SLURM_JOB_NAME"
echo "Node List   : $SLURM_JOB_NODELIST"
echo "Num Tasks   : $SLURM_NTASKS total [$SLURM_NNODES nodes @ $SLURM_CPUS_ON_NODE CPUs/node With $SLURM_CPUS_PER_TASK CPUs/task]"
echo "======================================================"
echo ""

module load hmmer

CPUS=$SLURM_CPUS_PER_TASK

HMM_DIR=results/HMMs
OUTDIR=results/GTDB/bac120_ar53-i2
rm -r $OUTDIR
mkdir -p $OUTDIR

#Combine anf/nif/vnf HMMs
cat $HMM_DIR/anf*-gtdb*.hmm $HMM_DIR/nif*-gtdb*.hmm $HMM_DIR/vnf*-gtdb*.hmm > $HMM_DIR/merged-anf_nif_vnf_gtdb.hmm

#Combine nfl/chl HMMs
cat $HMM_DIR/nfl*-gtdb*.hmm $HMM_DIR/ChIl*-gtdb*.hmm > $HMM_DIR/merged-nfl_chl_gtdb.hmm

#HMM search
for file in $GTDB_PATH/*; do 
        f="${file##*/}"
        hmmsearch --cpu $CPUS $HMM_DIR/merged-anf_nif_vnf_gtdb.hmm "$file" > "$OUTDIR/${f%.faa}_anf_nif_vnf-gtdb.out"
        hmmsearch --cpu $CPUS $HMM_DIR/merged-nfl_chl_gtdb.hmm "$file" > "$OUTDIR/${f%.faa}_nfl_chl-gtdb.out"
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


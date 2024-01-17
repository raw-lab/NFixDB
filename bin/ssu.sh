#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=ssu
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

# rsync -a /projects/raw_lab/databases/GTDB/protein_fna_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_fna_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined

mkdir -p SSUs

genomes=$(cut -f2 TSVs/filteredhits.tsv) #column with genome IDs (GB_GCA_018902765.1)

module load anaconda3
conda activate barrnap 

echo "Running barrnap..."
for g in $genomes
do
    cat /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined/"$g"_protein.fna | barrnap -o ./SSUs/"$g".faa
done

echo "Done"

echo "Running ssu.py..."
python3 scripts/ssu.py

echo "All Done"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


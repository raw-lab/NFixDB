#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=tax
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
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

# Get full taxonomy
echo "Running taxonomy.py..."

python3 scripts/taxonomy.py

echo "taxonomy.py done"
echo ""

# Find top hits
echo "Running tophits.py..."

python3 scripts/tophits.py
rm hits_temp.tsv
rm hits_temp2.tsv

echo "tophits.py done"
echo ""

# Find better top hits for fastas
echo "Running topfastas.py..."

python3 scripts/topfastas.py
rm fasta_temp.tsv
rm fasta_temp2.tsv

echo "topfastas.py done"
echo ""

# Filter the top hits and fasta hits
echo "Running analysis..."

python3 scripts/analysis.py
echo ""
python3 scripts/analysis_fasta.py

echo "Analysis done"
echo ""

# Remake fastas
echo "Making new fastas..."

python3 scripts/nitrogenase_fastas.py

echo "Fastas done"
echo ""

# Cluster new fastas
module load cd-hit
echo "Clustering fastas..."

for file in fastas/R2/final/*; do
    cd-hit -i "$file" -o "clusters/R2/final/${file%.faa}_100" -c 1.00
    cd-hit -i "$file" -o "clusters/R2/final/${file%.faa}_99" -c 0.99
    cd-hit -i "$file" -o "clusters/R2/final/${file%.faa}_97" -c 0.97
done

echo "Clustering done"
echo ""

echo "All done!"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


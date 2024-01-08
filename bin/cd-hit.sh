#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=cd-hit
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

module load cd-hit

# # Iteration 2 clusters
# for file in fastas/R2/i2-2/*; do
#    cd-hit -i "$file" -o "clusters/R2/i2-2/$(basename -- $file)_100.faa" -c 1.00
#    cd-hit -i "$file" -o "clusters/R2/i2-2/$(basename -- $file)_99.faa" -c 0.99
#    cd-hit -i "$file" -o "clusters/R2/i2-2/$(basename -- $file)_97.faa" -c 0.97
# done

# # Iteration 3 clusters
# for file in fastas/R2/i2-3/*; do
#    cd-hit -i "$file" -o "clusters/R2/i2-3/$(basename -- $file)_100.faa" -c 1.00
#    cd-hit -i "$file" -o "clusters/R2/i2-3/$(basename -- $file)_99.faa" -c 0.99
#    cd-hit -i "$file" -o "clusters/R2/i2-3/$(basename -- $file)_97.faa" -c 0.97
# done

# # Final clusters
# for file in fastas/R2/final/*; do
#    cd-hit -i "$file" -o "clusters/R2/final/$(basename -- $file)_100.faa" -c 1.00
#    cd-hit -i "$file" -o "clusters/R2/final/$(basename -- $file)_99.faa" -c 0.99
#    cd-hit -i "$file" -o "clusters/R2/final/$(basename -- $file)_97.faa" -c 0.97
# done

# Nucleotide clusters
for file in fastas/R2/final_nuc/*; do
   cd-hit-est -i "$file" -o "clusters/R2/final_nuc/$(basename -- $file)_100.fna" -c 1.00
   cd-hit-est -i "$file" -o "clusters/R2/final_nuc/$(basename -- $file)_99.fna" -c 0.99
   cd-hit-est -i "$file" -o "clusters/R2/final_nuc/$(basename -- $file)_97.fna" -c 0.97
done

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

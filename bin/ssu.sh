#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=NFixDB-ssu
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

#rsync -a ../databases/GTDB/gtdb_genomes_reps_r207/archaea/ ../databases/GTDB/gtdb_genomes_reps_r207/bacteria/ ../databases/GTDB/gtdb_genomes_reps_r207-combined

#mkdir -p SSUs

#genomes=$(cut -f2 filteredhits_i3.tsv)
#accArr=()
#fnaext=".fna"

#for g in $genomes
#do
#    acc=$(echo "$g" | cut -c4-18)
#    accArr+=("$acc")
#done

#for genome in "${accArr[@]}"
#do
#    fna="${genome}${fnaext}"
#    barrnap -o ./SSUs/"$genome".faa < ../databases/GTDB/gtdb_genomes_reps_r207-combined/"$fna"
#done

sed -i 's/GB_//g' filteredhits_i3_full.tsv
sed -i 's/RS_//g' filteredhits_i3_full.tsv
python3 SSU_int.py

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""


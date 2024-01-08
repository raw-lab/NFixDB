#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=oDB-cd-hit
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

# Buckley
echo "Clustering Buckley..."

cd-hit -i "../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa" -o "clusters/R2/oDB/Buckley_nifH_100" -c 1.00
cd-hit -i "../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa" -o "clusters/R2/oDB/Buckley_nifH_99" -c 0.99
cd-hit -i "../outside_dbs/Buckley/nifH_best_2012_BucDB_pro_prodigal.faa" -o "clusters/R2/oDB/Buckley_nifH_97" -c 0.97

echo "Done"

# FunGene
echo "Clustering FunGene..."

cd-hit -i "../outside_dbs/FunGene/FunGene_nifD-seeds.faa" -o "clusters/R2/oDB/FunGene_nifD_100" -c 1.00
cd-hit -i "../outside_dbs/FunGene/FunGene_nifD-seeds.faa" -o "clusters/R2/oDB/FunGene_nifD_99" -c 0.99
cd-hit -i "../outside_dbs/FunGene/FunGene_nifD-seeds.faa" -o "clusters/R2/oDB/FunGene_nifD_97" -c 0.97

cd-hit -i "../outside_dbs/FunGene/FunGene_nifH-seeds.faa" -o "clusters/R2/oDB/FunGene_nifH_100" -c 1.00
cd-hit -i "../outside_dbs/FunGene/FunGene_nifH-seeds.faa" -o "clusters/R2/oDB/FunGene_nifH_99" -c 0.99
cd-hit -i "../outside_dbs/FunGene/FunGene_nifH-seeds.faa" -o "clusters/R2/oDB/FunGene_nifH_97" -c 0.97

cd-hit -i "../outside_dbs/FunGene/FunGene_vnfD-seeds.faa" -o "clusters/R2/oDB/FunGene_vnfD_100" -c 1.00
cd-hit -i "../outside_dbs/FunGene/FunGene_vnfD-seeds.faa" -o "clusters/R2/oDB/FunGene_vnfD_99" -c 0.99
cd-hit -i "../outside_dbs/FunGene/FunGene_vnfD-seeds.faa" -o "clusters/R2/oDB/FunGene_vnfD_97" -c 0.97

echo "Done"

# Mise
echo "Clustering Mise..."

cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T1_100" -c 1.00
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T1_99" -c 0.99
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T1_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T1_97" -c 0.97

cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T2_100" -c 1.00
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T2_99" -c 0.99
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T2_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T2_97" -c 0.97

cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T3_100" -c 1.00
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T3_99" -c 0.99
cd-hit -i "../outside_dbs/Mise_classification/fastas/Mise_T3_noDup.fa" -o "clusters/R2/oDB/Mise_nifH_T3_97" -c 0.97

echo "Done"

# Zehr
echo "Clustering Zehr..."

cd-hit -i "../outside_dbs/Zehr/ZehrDB_nifH_prod.faa" -o "clusters/R2/oDB/Zehr_nifH_100" -c 1.00
cd-hit -i "../outside_dbs/Zehr/ZehrDB_nifH_prod.faa" -o "clusters/R2/oDB/Zehr_nifH_99" -c 0.99
cd-hit -i "../outside_dbs/Zehr/ZehrDB_nifH_prod.faa" -o "clusters/R2/oDB/Zehr_nifH_97" -c 0.97

echo "All Done"

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""

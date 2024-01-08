#!/bin/bash

# Load modules
module load mafft
module load hmmer

# Submit scripts
sbatch anf.sh 
sbatch chlB.sh 
sbatch chlN.sh 
sbatch chIl.sh 
sbatch nfl.sh 
sbatch nifH.sh
sbatch nifD.sh
sbatch nifK.sh
sbatch vnf.sh 
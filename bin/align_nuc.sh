#!/bin/bash

# Load modules
module load mafft

# Submit scripts
sbatch anf_nuc.sh 
sbatch chlB_nuc.sh 
sbatch chlN_nuc.sh 
sbatch chIl_nuc.sh 
sbatch nfl_nuc.sh 
sbatch nifH_nuc.sh
sbatch nifD_nuc.sh
sbatch nifK_nuc.sh
sbatch vnf_nuc.sh
#!/bin/bash

module load hmmer

sbatch scripts/oDB_hmm.sh
sbatch scripts/oDB_cluster-hmm.sh
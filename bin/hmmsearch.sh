#!/bin/bash

HMM_DIR=$1
OUT_DIR=$2
GTDB_PATH=$3
CPUS=$4

#Combine anf/nif/vnf HMMs
cat $HMM_DIR/anf*.hmm $HMM_DIR/nif*.hmm $HMM_DIR/vnf*.hmm > $HMM_DIR/merged-anf_nif_vnf.hmm

#Combine nfl/chl HMMs
cat $HMM_DIR/nfl*.hmm $HMM_DIR/ChIl*.hmm > $HMM_DIR/merged-nfl_chl.hmm

rm -rf $OUT_DIR
mkdir -p $OUT_DIR

#HMM search
for file in $GTDB_PATH/archaea/* $GTDB_PATH/bacteria/*; do
        f="${file##*/}"
        hmmsearch --cpu $CPUS $HMM_DIR/merged-anf_nif_vnf.hmm "$file" > "$OUT_DIR/${f%.faa}_anf_nif_vnf.out"
        hmmsearch --cpu $CPUS $HMM_DIR/merged-nfl_chl.hmm "$file" > "$OUT_DIR/${f%.faa}_nfl_chl.out"
done

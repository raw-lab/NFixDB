#!/bin/bash

### Program arguments: ###
SEEDS=$1
ALIGN_DIR=$2
HMM_DIR=$3
CPUS=$4

mkdir -p $ALIGN_DIR
mkdir -p $HMM_DIR


#anf
echo "======================================================"
echo "Aligning and building anf   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/anfD_*.faa > $ALIGN_DIR/anfD-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/anfH_*.faa > $ALIGN_DIR/anfH-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/anfK_*.faa > $ALIGN_DIR/anfK-aln.faa

hmmbuild --cpu $CPUS $HMM_DIR/anfD.hmm $ALIGN_DIR/anfD-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/anfH.hmm $ALIGN_DIR/anfH-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/anfK.hmm $ALIGN_DIR/anfK-aln.faa

#nif
echo "======================================================"
echo "Aligning and building nif   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nifH_*.faa > $ALIGN_DIR/nifH-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nifD_*.faa > $ALIGN_DIR/nifD-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nifK_*.faa > $ALIGN_DIR/nifK-aln.faa

hmmbuild --cpu $CPUS $HMM_DIR/nifH.hmm $ALIGN_DIR/nifH-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/nifD.hmm $ALIGN_DIR/nifD-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/nifK.hmm $ALIGN_DIR/nifK-aln.faa

#vnf
echo "======================================================"
echo "Aligning and building vnf   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/vnfD_*.faa > $ALIGN_DIR/vnfD-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/vnfH_*.faa > $ALIGN_DIR/vnfH-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/vnfK_*.faa > $ALIGN_DIR/vnfK-aln.faa

hmmbuild --cpu $CPUS $HMM_DIR/vnfD.hmm $ALIGN_DIR/vnfD-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/vnfH.hmm $ALIGN_DIR/vnfH-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/vnfK.hmm $ALIGN_DIR/vnfK-aln.faa

#Chl
echo "======================================================"
echo "Aligning and building Chl   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/ChIl-Bchl_*.faa > $ALIGN_DIR/ChIl-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/ChlN-BchN_*.faa > $ALIGN_DIR/ChlN-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/ChlB-BchB_*.faa > $ALIGN_DIR/ChlB-aln.faa

hmmbuild --cpu $CPUS $HMM_DIR/ChIl.hmm $ALIGN_DIR/ChIl-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/ChlN.hmm $ALIGN_DIR/ChlN-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/ChlB.hmm $ALIGN_DIR/ChlB-aln.faa

#nfl
echo "======================================================"
echo "Aligning and building nfl   : $(date)"

mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nflD_*.faa > $ALIGN_DIR/nflD-aln.faa
mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nflH_*.faa > $ALIGN_DIR/nflH-aln.faa

hmmbuild --cpu $CPUS $HMM_DIR/nflD.hmm $ALIGN_DIR/nflD-aln.faa
hmmbuild --cpu $CPUS $HMM_DIR/nflH.hmm $ALIGN_DIR/nflH-aln.faa



import gzip
from pathlib import Path
import subprocess
import pyhmmer


def align(seed_file, aligned_output, threads=4):
	seed_file = Path(seed_file)
	aligned_output = Path(aligned_output)
	aligned_output.parent.mkdir(parents=True, exist_ok=True)

	# mafft --thread $CPUS --localpair --maxiterate 1000 $SEEDS/nifH*.faa > $ALIGN_DIR/nifH-aln.faa
	cmd = ["mafft", "--localpair", "--maxiterate", "1000", "--thread", f"{threads}", str(seed_file)]
	out = aligned_output.open('w')
	p = subprocess.run(cmd, stdout=out, stderr=subprocess.PIPE)
	#if p.returncode != 0:
	#	print("Error in MAFFT alignment:")
	#	print(p.stderr)

	return aligned_output


def create_hmm(seed_file, hmm_output, CPUs=4):
	seed_file = Path(seed_file)
	hmm_output = Path(hmm_output)
	hmm_output.mkdir(parents=True, exist_ok=True)

	outfile = hmm_output/f"{seed_file.stem}.hmm"
	if outfile.exists():
		return outfile

	alpha = pyhmmer.easel.Alphabet.amino()
	MSAFile = pyhmmer.easel.MSAFile
	DigitalMSA = pyhmmer.easel.DigitalMSA
	builder = pyhmmer.plan7.Builder(alphabet=alpha)
	background = pyhmmer.plan7.Background(alpha)


	if seed_file.stat().st_size > 0:
		alignment = align(seed_file, hmm_output/f"{seed_file.stem}.aln", threads=CPUs)

		with MSAFile(alignment, alphabet=alpha) as msa_file:
			msa = msa_file.read()
		msa.name = seed_file.stem.encode()
		msa_d = msa.digitize(alpha)

		hmm, _, _ = builder.build_msa(msa_d, background)
		#hmm.name = seed_file.stem.encode()

		with open(outfile, "wb") as hmm_file:
			hmm.write(hmm_file)
	return outfile


def hmmscan(protein_path, outpath, hmm, CPUs=4, minscore=30, evalue=1e-10):
	# HMMER
	outpath = Path(outpath)
	outpath.mkdir(parents=True, exist_ok=True)
	#errfile=outfile.with_suffix('.err').open('w')
	alphabet = pyhmmer.easel.Alphabet.amino()
	file_list = Path(protein_path).glob('*/*.faa*')
	#print("Scanning", len(file_list), "files")
	for amino in file_list:
		outfile = Path(outpath) / f"{amino.stem}-{hmm.stem}.tsv"
		if outfile.exists():
			continue

		tmpfile = outfile.with_suffix(".tmp")
		if amino.suffix == ".gz":
			amino_file = gzip.open(amino, "rt")
		else:
			amino_file = open(amino, "rt")
		
		with open(tmpfile, 'wt') as hmm_writer, pyhmmer.plan7.HMMFile(hmm) as hmm_reader:
			seq_reader = list()
			line = amino_file.readline()
			while line:
				if line.startswith(">"):
					header,description = line.strip().split(maxsplit=1)
					seq = list()
					line = amino_file.readline()
					while line and not line.startswith(">"):
						seq += [line.strip()]
						line = amino_file.readline()
					seq = "".join(seq)
					txt_seq = pyhmmer.easel.TextSequence(sequence=seq, name=header[1:].encode(), description=description.encode())
					seq_reader += [txt_seq.digitize(alphabet)]
				else:
					line = amino_file.readline()

			for hit in pyhmmer.hmmer.hmmsearch(hmm_reader, seq_reader, E=evalue, cpus=CPUs):
				for h in hit:
					for domain in h.domains.included:
						if domain.score < minscore:
							continue
						align = domain.alignment
						query_name = hit.query.name.decode()
						print( 
							query_name, 
							h.name.decode(), 
							f'{h.evalue:.1E}', 
							f"{h.score:.1f}", 
							len(align.hmm_sequence),
							h.description.decode(),
							sep='\t', file=hmm_writer)
		#if tmpfile.stat().st_size > 0:
		tmpfile.rename(outfile)
		#else:
		#	tmpfile.unlink(missing_ok=True)

	return

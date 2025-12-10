
from pathlib import Path
import subprocess as sp


def check_fastas_with_cerberus(fasta_folder:Path, cerberus_db:Path, output_folder:Path, cpus:int=4):
	"""
	Check FASTA files against the Cerberus database.

	Parameters:
	fasta_folder (Path): Path to the folder containing FASTA files.
	cerberus_db (Path): Path to the Cerberus database file.
	output_folder (Path): Path to the folder where results will be saved.
	"""
	output_folder.mkdir(parents=True, exist_ok=True)

	log = output_folder / f"stdout.log"
	# Placeholder for actual Cerberus checking logic
	with open(log, 'w') as out_f, log.with_name("stderr.log").open('w') as err_f:
		# Run Cerberus
		cmd = ["cerberus.py", "--protein", str(fasta_folder), "--hmm", "all", "--db", str(cerberus_db), "--dir-out", str(output_folder), "--cpus", str(cpus)]
		result = sp.run(cmd, stderr=err_f, stdout=out_f)

	return output_folder

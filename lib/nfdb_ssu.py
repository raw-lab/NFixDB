
import os
from pathlib import Path
import subprocess
import gzip
import pandas as pd


# rsync -a /projects/raw_lab/databases/GTDB/protein_fna_reps/bacteria/ /projects/raw_lab/databases/GTDB/protein_fna_reps/archaea/ /projects/raw_lab/databases/GTDB/protein_fna_reps_r214-combined


def generate_ssu(filteredhits_tsv, outpath, gtdb_fna, threads=4):
    outpath = Path(outpath)
    outpath.mkdir(parents=True, exist_ok=True)
    gtdb_fna = Path(gtdb_fna)

    genomes = list()
    with open(filteredhits_tsv, 'r') as reader:
        reader.readline()  # skip header
        for line in reader:
            genome_id = line.split('\t')[0]
            genomes += [genome_id]


    print("Running barrnap on Genomes in GTDB")
    for g in genomes:
        if Path(gtdb_fna, "archaea", f"{g}_protein.fna.gz").exists():
            infile = Path(gtdb_fna, "archaea", f"{g}_protein.fna.gz")
            kingdom = "arc"
        elif Path(gtdb_fna, "bacteria", f"{g}_protein.fna.gz").exists():
            infile = Path(gtdb_fna, "bacteria", f"{g}_protein.fna.gz")
            kingdom = "bac"
        else:
            print("ERROR: Genome not found in GTDB:", g)
            continue

        cmd = ["barrnap", "-o", f"{outpath}/{g}.faa", "--kingdom", kingdom, "--threads", str(threads)]
        out = open(f"{outpath}/{g}_barrnap.log", "w")
        err = open(f"{outpath}/{g}_barrnap.err", "w")
        subprocess.run(cmd, input=gzip.open(infile, "rt").read(), text=True, stdout=out, stderr=err)
        out.close()
        err.close()

    return outpath


def add_ssu_to_filteredhits(input_filteredhits, ssu_path, outfile):

    # Get filteredhits TSV
    df = pd.DataFrame(pd.read_table(input_filteredhits))

    # Create empty lists for each SSU
    s5 = []
    s58 = []
    s16 = []
    s23 = []

    ssu = pd.DataFrame(columns=['GenomeID', '5S', '5.8S', '16S', '23S'])

    # Populate SSU dataframe with SSUs that correspond to the genome ID
    directory = ssu_path
    for index, row in df.iterrows():
        ssu['GenomeID'] = df['GenomeID']
        for file in os.listdir(directory):
            f = os.path.join(directory, file)
            if os.path.isfile(f):
                base = os.path.splitext(file)[0]
                if base == row['GenomeID']:
                    with open(f, 'r') as fi:
                        for line in fi:
                            if line.startswith(">"):
                                split = line.split("::")
                                if '5S' in split[0]:
                                    s5.append(split[1].strip())
                                elif '5.8S' in split[0]:
                                    s58.append(split[1].strip())
                                elif '16S' in split[0]:
                                    s16.append(split[1].strip())
                                elif '23S' in split[0]:
                                    s23.append(split[1].strip())
                    ssu.loc[ssu['GenomeID']==row['GenomeID'], '5S'] = ', '.join(str(v) for v in s5)
                    ssu.loc[ssu['GenomeID']==row['GenomeID'], '5.8S'] = ', '.join(str(v) for v in s58)
                    ssu.loc[ssu['GenomeID']==row['GenomeID'], '16S'] = ', '.join(str(v) for v in s16)
                    ssu.loc[ssu['GenomeID']==row['GenomeID'], '23S'] = ', '.join(str(v) for v in s23)
                    s5.clear()
                    s58.clear()
                    s16.clear()
                    s23.clear()

    # Convert to TSV
    final_df = pd.merge(df, ssu, on = "GenomeID", how="left")
    final_df.to_csv(outfile, sep = "\t", index=False)

    return outfile

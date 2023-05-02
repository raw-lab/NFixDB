import pandas as pd
import os
import re
import subprocess

df = pd.DataFrame(pd.read_table('filteredhits_i3.tsv'))

#----------------------------------------------------------- BARRNAP SSUs -----------------------------------------------------------

directory = '/projects/raw_lab/databases/GTDB/gtdb_genomes_reps_r207-combined' 
for index, row in df.iterrows():
    reg = r'[\w]+_([\w]+_[\w]+.[\w])'
    regex = re.match(reg, row['GenomeID']).group(1)
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        if os.path.isfile(f):
            fi = regex + ".fna"
            if file == fi:
                command = f"barrnap -o ./SSUs/{regex}_SSUs.faa < {f}"
                subprocess.run(command, shell=True)
                print("yes")

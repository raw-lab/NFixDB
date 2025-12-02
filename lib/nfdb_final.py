
import pandas as pd
import sqlite3
from pathlib import Path


def finalize_database(tsv_path, output_tsv, output_sqlite):
    tsv_path = Path(tsv_path)

    filteredhits_SSU = tsv_path / "filteredhits_SSU.tsv"

    filthits = pd.DataFrame(pd.read_table(filteredhits_SSU))

    final = filthits[['GenomeID', 'nifH', 'EV_nifH', 'bitscore_nifH', 'location_nifH', 'alnLen_nifH', 'seqLen_nifH',
                                'nifD', 'EV_nifD', 'bitscore_nifD', 'location_nifD', 'alnLen_nifD', 'seqLen_nifD',
                                'nifK', 'EV_nifK', 'bitscore_nifK', 'location_nifK', 'alnLen_nifK', 'seqLen_nifK',
                                'anfH', 'EV_anfH', 'bitscore_anfH', 'location_anfH', 'alnLen_anfH', 'seqLen_anfH',
                                'anfD', 'EV_anfD', 'bitscore_anfD', 'location_anfD', 'alnLen_anfD', 'seqLen_anfD',
                                'anfK', 'EV_anfK', 'bitscore_anfK', 'location_anfK', 'alnLen_anfK', 'seqLen_anfK',
                                'vnfH', 'EV_vnfH', 'bitscore_vnfH', 'location_vnfH', 'alnLen_vnfH', 'seqLen_vnfH',
                                'vnfD', 'EV_vnfD', 'bitscore_vnfD', 'location_vnfD', 'alnLen_vnfD', 'seqLen_vnfD',
                                'vnfK', 'EV_vnfK', 'bitscore_vnfK', 'location_vnfK', 'alnLen_vnfK', 'seqLen_vnfK',
                                'nflH', 'EV_nflH', 'bitscore_nflH', 'location_nflH', 'alnLen_nflH', 'seqLen_nflH',
                                'nflD', 'EV_nflD', 'bitscore_nflD', 'location_nflD', 'alnLen_nflD', 'seqLen_nflD',
                                'ChlB', 'EV_ChlB', 'bitscore_ChlB', 'location_ChlB', 'alnLen_ChlB', 'seqLen_ChlB',
                                'ChlL', 'EV_ChlL', 'bitscore_ChlL', 'location_ChlL', 'alnLen_ChlL', 'seqLen_ChlL',
                                'ChlN', 'EV_ChlN', 'bitscore_ChlN', 'location_ChlN', 'alnLen_ChlN', 'seqLen_ChlN',
                                'GTDB_Tax', 'NCBI_TaxID', 'NCBI_Tax', '5S', '5.8S', '16S', '23S']]


    final.to_csv(output_tsv, sep="\t", index=False)


    # Create SQLite database and import final TSV
    connection = sqlite3.connect(output_sqlite)
    cursor = connection.cursor()

    #------------------------------------------------------EVALUE TAXONOMY------------------------------------------------------
    cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, Location varchar, AlnLength number, SeqLength number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
    connection.commit()
    evalue_df = pd.DataFrame(pd.read_table(f'{tsv_path}/evalue_taxonomy.tsv'))
    evalue_df.to_sql('evalue_taxonomy', connection, if_exists = 'replace')

    #------------------------------------------------------TOP HITS TAXONOMY------------------------------------------------------ 
    cursor.execute('CREATE TABLE IF NOT EXISTS tophits (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
    connection.commit()
    tophits_df = pd.DataFrame(pd.read_table(f'{tsv_path}/tophits.tsv'))
    tophits_df.to_sql('tophits', connection, if_exists = 'replace')

    #----------------------------------------------------FILTERED HITS TAXONOMY----------------------------------------------------
    cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits (GenomeID varchar, GTDB_Tax varchar, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number)')
    connection.commit()
    filteredhits_df = pd.DataFrame(pd.read_table(f'{tsv_path}/filteredhits.tsv'))
    filteredhits_df.to_sql('filteredhits', connection, if_exists = 'replace')

    #------------------------------------------------------TOP FASTA TAXONOMY------------------------------------------------------ 
    cursor.execute('CREATE TABLE IF NOT EXISTS topfasta (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number)')
    connection.commit()
    topfasta_df = pd.DataFrame(pd.read_table(f'{tsv_path}/topfasta.tsv'))
    topfasta_df.to_sql('topfasta', connection, if_exists = 'replace')

    #------------------------------------------------------FILTERED FASTA TAXONOMY------------------------------------------------------
    cursor.execute('CREATE TABLE IF NOT EXISTS filteredfasta (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfH varchar, vnfD varchar, vnfK varchar, anfH varchar, anfD varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
    connection.commit()
    filteredfasta_df = pd.DataFrame(pd.read_table(f'{tsv_path}/filteredfasta.tsv'))
    filteredfasta_df.to_sql('filteredfasta', connection, if_exists = 'replace')

    #------------------------------------------------------NFIXDB------------------------------------------------------
    cursor.execute('CREATE TABLE IF NOT EXISTS NFixDB (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar, [5S] varchar, [5.8S] varchar, [16S] varchar, [23S] varchar)')
    connection.commit()
    evalue_df = pd.DataFrame(pd.read_table(output_tsv))
    evalue_df.to_sql('NFixDB', connection, if_exists = 'replace')


    return output_tsv

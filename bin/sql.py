import pandas as pd
import sqlite3

connection = sqlite3.connect('NFixDB.db')
cursor = connection.cursor()

#------------------------------------------------------EVALUE TAXONOMY------------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy.tsv'))
evalue_df.to_sql('evalue_taxonomy', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy_i2 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue2_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i2.tsv')).drop(columns='Unnamed: 0')
evalue2_df.to_sql('evalue_taxonomy_i2', connection, if_exists = 'replace')
#i3 
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy_i3 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue3_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i3.tsv')).drop(columns='Unnamed: 0')
evalue3_df.to_sql('evalue_taxonomy_i3', connection, if_exists = 'replace')

#------------------------------------------------------OOR TAXONOMY------------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS oor_taxonomy (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
oor_df = pd.DataFrame(pd.read_table('TSVs/oor_taxonomy.tsv'))
oor_df.to_sql('oor_taxonomy', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS oor_taxonomy_i2 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
oor2_df = pd.DataFrame(pd.read_table('TSVs/oor_taxonomy_i2.tsv')).drop(columns='Unnamed: 0')
oor2_df.to_sql('oor_taxonomy_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS oor_taxonomy_i3 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
oor3_df = pd.DataFrame(pd.read_table('TSVs/oor_taxonomy_i3.tsv')).drop(columns='Unnamed: 0')
oor3_df.to_sql('oor_taxonomy_i3', connection, if_exists = 'replace')

#------------------------------------------------------TOP HITS TAXONOMY------------------------------------------------------ 
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS tophits (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits_df = pd.DataFrame(pd.read_table('TSVs/tophits.tsv'))
tophits_df.to_sql('tophits', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS tophits_i2 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits2_df = pd.DataFrame(pd.read_table('TSVs/tophits_i2.tsv'))
tophits2_df.to_sql('tophits_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS tophits_i3 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits3_df = pd.DataFrame(pd.read_table('TSVs/tophits_i3.tsv'))
tophits3_df.to_sql('tophits_i3', connection, if_exists = 'replace')

#----------------------------------------------------FILTERED HITS TAXONOMY----------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
filteredhits_df = pd.DataFrame(pd.read_table('TSVs/filteredhits.tsv'))
filteredhits_df.to_sql('filteredhits', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i2 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
filteredhits2_df = pd.DataFrame(pd.read_table('TSVs/filteredhits_i2.tsv'))
filteredhits2_df.to_sql('filteredhits_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i3 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
filteredhits3_df = pd.DataFrame(pd.read_table('TSVs/filteredhits_i3.tsv'))
filteredhits3_df.to_sql('filteredhits_i3', connection, if_exists = 'replace')

#------------------------------------------------------TOP FASTA TAXONOMY------------------------------------------------------ 
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
topfasta_df = pd.DataFrame(pd.read_table('TSVs/topfasta.tsv'))
topfasta_df.to_sql('topfasta', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta_i2 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
topfasta2_df = pd.DataFrame(pd.read_table('TSVs/topfasta_i2.tsv'))
topfasta2_df.to_sql('topfasta_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta_i3 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
topfasta3_df = pd.DataFrame(pd.read_table('TSVs/topfasta_i3.tsv'))
topfasta3_df.to_sql('topfasta_i3', connection, if_exists = 'replace')

#------------------------------------------------------MERGE FASTA TAXONOMY------------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS mergefasta (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta_df = pd.DataFrame(pd.read_table('TSVs/mergefasta.tsv'))
mergefasta_df.to_sql('mergefasta', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS mergefasta_i2 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta2_df = pd.DataFrame(pd.read_table('TSVs/mergefasta_i2.tsv'))
mergefasta2_df.to_sql('mergefasta_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS mergefasta_i3 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfD varchar, vnfH varchar, vnfK varchar, anfD varchar, anfH varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta3_df = pd.DataFrame(pd.read_table('TSVs/mergefasta_i3.tsv'))
mergefasta3_df.to_sql('mergefasta_i3', connection, if_exists = 'replace')

#------------------------------------------------------LENGTHS------------------------------------------------------
cursor.execute('CREATE TABLE IF NOT EXISTS lengths_i3 (GenomeID varchar, GeneName varchar, SeqID varchar, AlnLength number, SeqLength number)')
connection.commit()
lengths_i3_df = pd.DataFrame(pd.read_table('lengths_i3.tsv'))
lengths_i3_df.to_sql('lengths_i3', connection, if_exists = 'replace')

#------------------------------------------------------SSU------------------------------------------------------
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i3_wSSU (GenomeID varchar, GTDB_Tax varchar, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, nifD varchar, EV_nifD float, bitscore_nifD float, nifK varchar, EV_nifK float, bitscore_nifK float, anfH varchar, EV_anfH float, bitscore_anfH float, anfD varchar, EV_anfD float, bitscore_anfD float, anfK varchar, EV_anfK float, bitscore_anfK float, vnfH varchar, EV_vnfH float, bitscore_vnfH float, vnfD varchar, EV_vnfD float, bitscore_vnfD float, vnfK varchar, EV_vnfK float, bitscore_vnfK float, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float, [5S] varchar, [5.8S] varchar, [16S] varchar, [23S] varchar)')
connection.commit()
ssu_df = pd.DataFrame(pd.read_table('filteredhits_i3_wSSU.tsv')).drop(columns='Unnamed: 0')
ssu_df.to_sql('filteredhits_i3_wSSU', connection, if_exists = 'replace')

#------------------------------------------------------MISE CLASSIFICATION------------------------------------------------------
#       Gene	MiseClass	SeqID	EValue	Bitscore
#cursor.execute('CREATE TABLE IF NOT EXISTS Mise_class (GenomeID varchar)')
#connection.commit()
#Mise_class_df = pd.DataFrame(pd.read_table('Mise_class.tsv'))
#Mise_class_df.to_sql('Mise_class', connection, if_exists = 'replace')

#------------------------------------------------------NFIXDB------------------------------------------------------
cursor.execute('CREATE TABLE IF NOT EXISTS NFixDB (GenomeID varchar, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, alnLen_nifH number, seqLen_nifH number,nifD varchar, EV_nifD float, bitscore_nifD float, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, alnLen_nflD number, seqLen_nflD number, nflH varchar, EV_nflH float, bitscore_nflH float, alnLen_nflH number, seqLen_nflH number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, alnLen_ChlN number, seqLen_ChlN number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, alnLen_ChIl number, seqLen_ChIl number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, alnLen_ChlB number, seqLen_ChlB number, [5S] varchar, [5.8S] varchar, [16S] varchar, [23S] varchar)')
connection.commit()
evalue_df = pd.DataFrame(pd.read_table('NFixDB.tsv'))
evalue_df.to_sql('NFixDB', connection, if_exists = 'replace')

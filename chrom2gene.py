import csv
from cruzdb import Genome

# python2 -m pip install --upgrade pip
# python2 -m pip install setuptools # first 2 may be already installed
# python2 -m pip install cruzdb
# python2 -m pip install sqlalchemy

# MySQLdb stuff:
# sudo apt-get install mysql-server
# sudo apt-get install libmysqlclient-dev # gives us mysql_config
# FINALLY download MySQLdb source, do process described in INSTALL file

hg19 = Genome('hg19')
INPUTFILE = "suggestive.pheno_simple.covar_none.test_wald.csv"
filereader = csv.reader(open(INPUTFILE))

chrom_i = None
pos_i = None
for i, line in enumerate(filereader):
    if i == 0:
        # CHROM POS REF ALT N_INFORMATIVE Test Beta SE Pvalue PVALUE
        chrom_i = line.index('CHROM')
        pos_i = line.index('POS')
        continue
    chrom = 'chr' + str(line[chrom_i])
    pos = int(line[pos_i])
    start = pos - 50
    end = pos + 50
    print chrom, start, end
    genes = hg19.bin_query('refGene', chrom, start, end)
    print set(g.name2 for g in genes)
    if i > 4:
        break

quit()

for i, line in enumerate(open(INPUTFILE)):
    toks = line.split()
    if i == 0:
        print "\t".join(['gene'] + toks)
    else:
        chrom, posns = toks[0].split(":")
        start, end = map(int, posns.rstrip("|").split("-"))
        genes = hg19.bin_query('refGene', chrom, start, end)
        print "\t".join(["|".join(set(g.name2 for g in genes))] + toks)

import csv
from cruzdb import Genome


# python2 -m pip install --upgrade pip
#   572  python2 -m pip install setuptools
#   573  python2 -m pip install cruzdb
#   575  python2 -m pip install sqlalchemy
#   581  python2 -m pip install MySQLdb

# sudo apt-get install mysql-server
# sudo apt-get install libmysqlclient-dev # gives us mysql_config
# download the MySQLdb source and do process described in INSTALL file

hg19 = Genome('hg19')
INPUTFILE = "suggestive.pheno_simple.covar_none.test_wald.csv"
filereader = csv.reader(open(INPUTFILE))

for i, line in enumerate(filereader):
    if i < 4:
        print line

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

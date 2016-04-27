from glob import glob
from os.path import join
import re
BRIEFS = 'briefs'
filenames = glob(join(BRIEFS, '*.html'))

earliest_year = 2020
earliest_month = 13
earliest_day = 32

for fname in filenames:
	with open(fname, 'r') as rf:
		txt = rf.read()
		if re.search(r'\bISIS\b', txt) or re.search(r'\bISIL\b', txt):
			year = int(fname[24:28])
			month = int(fname[29:31])
			day = int(fname[32:34])
			if year <= earliest_year:
				if month<=earliest_month:
					if day<=earliest_day:
						earliest_year = year
						earliest_month = month
						earliest_day = day

print("The first time the White House mentioned ISIS/ISIL was: "+str(earliest_month)+"/"
	+str(earliest_day)+"/"+str(earliest_year))
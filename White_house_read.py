from glob import glob
from os.path import join
import re
BRIEFS = 'briefs'
filenames = glob(join(BRIEFS, '*.html'))


for fname in filenames
	with open(fname, 'r') as rf:
		txt = rf.read()
		if re.search(r'\bISIS\b', txt) or re.search(r'\bISIL\b', txt):
			print(fname, "mentions ISIS/ISIL")
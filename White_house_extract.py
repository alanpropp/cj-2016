from bs4 import BeautifulSoup
from glob import glob
from os.path import join
from urllib.parse import urljoin
import requests
from os import makedirs

INDEX_PAGES_DIR = 'index-pages'
base_URL = 'https://www.whitehouse.gov/briefing-room/press-briefings/'
file_names = glob(join(INDEX_PAGES_DIR, '*.html'))

BRIEFS = 'briefs'
makedirs(BRIEFS, exist_ok=True)

for fname in file_names:
	# Get the text from the file
	with open(fname, 'r') as rf:
		txt = rf.read()
		# Turn it into soup
	soup = BeautifulSoup(txt, 'lxml')
	# Extract the URLs
	for h in soup.find_all('h3'):
		href = h.find('a').attrs['href']
		url = urljoin(base_URL, href)
		print("Downloading from...", url)
		resp = requests.get(url)
		# create a filename from the relative href path
		fn = href.replace('/', '-').strip('-') + '.html'
		full_fname = join(BRIEFS, fn)
		print("Saving to...", full_fname)
		with open(full_fname, 'w') as wf:
			wf.write(resp.text)
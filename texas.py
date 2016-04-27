import requests
from os import makedirs
from os.path import join
from glob import glob
from bs4 import BeautifulSoup
from glob import glob
from os.path import join
from urllib.parse import urljoin
import requests
from os import makedirs

links = []
BASE_URL = 'http://www.tdcj.state.tx.us/death_row/'
FIRST_URL = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
resp = requests.get(FIRST_URL)
txt = resp.text
soup = BeautifulSoup(txt, 'lxml')

#Go through all the links to last word statements
for h in soup.find_all('td'):
	#Some do not have last word pages and go to a default page (so no attributes)
	try:
		href = h.find('a').attrs['href']
		url = urljoin(BASE_URL, href)
		if "last.html" in url:
			links.append(url)
	except Exception:
		pass

for link in links:
	resp = requests.get(link)
	txt = resp.text
	#Check to make sure that religion is not mentioned
	if not "God" in txt and not "Jesus" in txt and not "Lord" in txt and not "Christ" in txt:
		soup = BeautifulSoup(resp.text, 'lxml')


		#Extract the name from the link
		for h in soup.find_all('body'):
			paragraphs = h.find_all('p')
			for p in paragraphs:
				name_string = str(p)
				if "#" in name_string and len(name_string)<75:
					name_string = name_string[3:].strip()
					name_string = name_string[:name_string.find("#")].strip()
					if "," in name_string[len(name_string)-1]:
						name_string = name_string[:-1].strip()
					print(name_string)

import requests
import os
import csv
import pdfplumber


links = ['http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn13.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn14.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/WARN_Interim_041614_to_063014.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/WARNReportfor7-1-2014to06-30-2015.pdf']

files = []
year = 12

for link in links:
	pdf_fname = 'CAWARN-eddwarncn' + str(year) + '.pdf'
	files.append(pdf_fname)
	resp = requests.get(link)
	with open(pdf_fname, 'wb') as f:
		f.write(resp.content)
	year+=1

for file_name in files:
	pdf_fname = file_name
	# open the pdf
	outfile = open('CAWARN-all-pages.csv', 'w')
	outcsv = csv.writer(outfile)
	pdf = pdfplumber.open(pdf_fname)
	for page in pdf.pages:
		table = page.extract_table()
		for row in table[1:]:
			outcsv.writerow(row)
	outfile.close
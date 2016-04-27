import requests
from csv import DictReader
from shutil import unpack_archive
import os
import csv

url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2012_sqf_csv.zip'
resp = requests.get(url)
with open('NYPD_2012_ZIP', 'wb') as f:
    f.write(resp.content)

unpack_archive('NYPD_2012_ZIP', format = 'zip')

with open('2012.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader, None)
	for line in reader:
		date = line[3]
		sex = line[80]
		race = line[81]
		age = line[83]
		city = line[100] 
		if date == '6032012': #Date of the incident
			if sex == 'M': #He is male
				if race == 'B': #He is black
					if age == '17': #Repeatedly cites him as a 17-year-old
						if city == 'MANHATTAN': #It says he is a Harlem teen walking home - assume Manhattan
							print("This could be Alvin")

#This gives me several results, but I couldn't think of how to narrow it down any further!
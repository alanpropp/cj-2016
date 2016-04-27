import requests
import os
import csv

#url = "https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf"
#resp = requests.get(url)

#with open('breach.csv', 'w') as f:
#    f.write(resp.text)

def get_year(date):
	parentheses = 0
	year = ""
	for letter in date:
		if parentheses==2:
			year+=letter
		if letter == "/":
			parentheses+=1
	return year


total = 0
dictionary = {}
paper = 0
electronic = 0

with open('breach_report.csv', 'r', encoding="latin1") as f:
	reader = csv.reader(f)
	next(reader, None)
	for line in reader:
		try:
			indiv_affected = int(line[3].strip())
			date = line[4]
			location = line[6]
			total+=indiv_affected
			year = get_year(date)
			if not dictionary.get(year):
				dictionary[year] = indiv_affected
			else:
				dictionary[year] += indiv_affected
			if "paper" in location.lower():
				paper+=1
			else:
				electronic+=1
		except:
			pass

print("Total individuals affected: " + str(total))
print("Total paper: "+ str(paper))
print("Total electronic: " + str(electronic))
for num in ['09', '10', '11', '12', '13', '14', '15', '16']:
	affected = dictionary.get(num)
	print("20" + str(num) + ": " + str(affected))




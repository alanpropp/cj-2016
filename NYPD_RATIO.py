import requests
import csv
#Start with getting the numbers for 2014 and printing the results to the screen
url = 'http://stash.compjour.org/samples/stops-and-frisks/2014-nypd.csv'
resp = requests.get(url)
with open('2014-nypd.csv', 'w') as f:
    f.write(resp.text)
innocent = 0
arrested = 0
with open('2014-nypd.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader, None)
	for line in reader:
		arst_made = line[14]
		if arst_made == 'N':
			innocent+=1
		else:
			arrested+=1

print("Innocent in 2014: " + str(innocent))
print("Arrested in 2014: " + str(arrested))
print("Percentage innocent: " + str((innocent/(innocent+arrested))*100))
#Then, here are the results for 2015! Tried throwing the two into a loop together but
#it made the process extremely slow
url = 'http://stash.compjour.org/samples/stops-and-frisks/2015-nypd.csv'
resp = requests.get(url)
with open('2015-nypd.csv', 'w') as f:
    f.write(resp.text)
innocent = 0
arrested = 0
with open('2015-nypd.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader, None)
	for line in reader:
		arst_made = line[14]
		if arst_made == 'N':
			innocent+=1
		else:
			arrested+=1

print("Innocent in 2015: " + str(innocent))
print("Arrested in 2015: " + str(arrested))
print("Percentage innocent: " + str((innocent/(innocent+arrested))*100))


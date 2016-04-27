import csv

total = 0

with open('warn-act-listings-2016-1.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader, None)
	for line in reader:
		if not line[4] == "":
			total+=int(line[4])

print("Total layoffs in 2016: " + str(total))
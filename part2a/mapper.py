#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

country_dict={}

for line in reader:
	airport_id=int(line[0])
	airport_type=str(line[1])
	airport_name=str(line[2])
	airport_lat=int(line[3])
	airport_long=int(line[4])
	airport_country=str(line[5])
	airport_region=str(line[6])

	if airport_country not in country_dict:
		country_dict[airport_country]=0

	country_dict[airport_country]+=1

for key in country_dict:
	print "{0}\t{1}".format(key,country_dict[key])

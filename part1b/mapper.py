#!/usr/bin/python

import sys
import csv



reader = csv.reader(sys.stdin, delimiter=',')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

type_dict={}

for line in reader:
	airport_id=int(line[0])
	airport_type=str(line[1])
	airport_name=str(line[2])
	airport_lat=int(line[3])
	airport_long=int(line[4])
	airport_country=str(line[5])
	airport_region=str(line[6])

	if airport_type not in type_dict:
		type_dict[airport_type]=0

	type_dict[airport_type]+=1

for key in type_dict:
	print "{0}\t{1}".format(key,type_dict[key])

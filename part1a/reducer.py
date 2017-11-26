#!/usr/bin/python

import sys

# Initialize the keys
country_dict={}

for line in sys.stdin:
	data = line.strip().split('\t')

	if len(data)!=2:
		continue

	thisCountry, thisNum = data

	if thisCountry not in country_dict:
		country_dict[thisCountry]=0

	country_dict[thisCountry]+=int(thisNum)

for key in country_dict:
	print "{0}\t{1}".format(key,country_dict[key])

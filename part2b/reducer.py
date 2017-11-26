#!/usr/bin/python

import sys

# Initialize the keys
region_dict={}

for line in sys.stdin:
	data = line.strip().split('\t')

	if len(data)!=2:
		continue

	airport_region, thisNum = data

	if airport_region not in region_dict:
		region_dict[airport_region]=0

	region_dict[airport_region]+=int(thisNum)

max_val=0
for key in region_dict:
	max_val = max(max_val,region_dict[key])

for key in region_dict:
	if max_val == region_dict[key]:
		print "{0}\t{1}".format(key,region_dict[key])

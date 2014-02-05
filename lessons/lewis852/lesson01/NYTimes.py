#!/usr/bin/python
# Import required libraries
from __future__ import division
import sys


# Start a counter and store the textfile in memory
age = 0
impressions = 0
clicks = 0 
oldest_person = [0]

lines = sys.stdin.readlines()
lines.pop(0)
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:
	clean_line = line.strip().split(',')
	impressions = impressions + int(clean_line[2])
	clicks = clicks + int(clean_line[3])
	age = age + int(clean_line[0])

	if int(clean_line[0]) > int(oldest_person[0]):
		oldest_person = clean_line
		print oldest_person

print 'Total Unique Visitors: ', n
print 'Total Impressions: ', impressions
print 'Average Age: ', age/n
print 'Average Clicks Per Impressions: ', clicks/impressions




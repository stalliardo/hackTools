#!/usr/bin/python3

import re

# Function returns four arrays of dictionaries containing the codes for 200, 300, 400 and 500 responses

# TODO end of program code report generator

# Get all codes and add to an array if
# Loop over and add a counter for each

def extractCodes(fileName):
	print("Running status code extraction")
	
	file = open("dirsearchResTest.txt", "r")
	
	twoResponses = []
	threeResponses = []
	fourResponses = []
	fiveResponses = []
	
	for line in file:
		twos = re.search("^2", line)
		threes = re.search("^3", line)
		fours = re.search("^4", line)
		fives = re.search("^5", line)
		
		url = line.strip().split()[2]
		code = line.strip().split()[0]
		string = code + " " + url
		
		if twos:
			twoResponses.append(string)
		if threes:
			threeResponses.append(string)
		if fours:
			fourResponses.append(string)
		if fives:
			fiveResponses.append(string)
		
	
	results = [
		twoResponses,
		threeResponses,
		fourResponses,
		fiveResponses
	]
		
	file.close()
	
	return results


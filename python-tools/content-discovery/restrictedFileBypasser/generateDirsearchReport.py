#!/usr/bin/python3

import argparse
import sys
import os
from termcolor import colored
import subprocess as sp
from progress.spinner import Spinner
from extractResponseCodes import extractCodes

parser = argparse.ArgumentParser()
parser.add_argument("domainFile", help="The name of the file containing the domains")
args = parser.parse_args()

endOfProgramReport = []

def loopResponseUrlsAndAddToFile(file, content):
	fileToAddTo = open(file, 'a')
	for url in content:
		fileToAddTo.write(url + "\n")
	fileToAddTo.close()
		
def generateDirectories(generatedDirsearchFile, domainName):
	
	FILE_SUFFIX = "ResponseURLS.txt"
						
	if not os.path.exists(generatedDirsearchFile):
		print("file: " + generatedDirsearchFile + " not found!\nContinuing on to next domain!")
		return

	# Running so file must exist...		
	print("generateDirectories called")
	print("checking file length...")
	lengthCommand = "cat " + generatedDirsearchFile + " | wc -l"
	fileLength = sp.getoutput(lengthCommand)
	
	print("length is: " + fileLength)
	
	if int(fileLength) == 0:
		print ("File has no content!\nContinuing on to next domain!")
		return
	
	# Here, so file must contain items
	print("Generating directory + ", domainName)
	
	# 1 get the current directory...
	currentDirectory = os.getcwd()
	folderPath = currentDirectory + "/RFB_Results"
	
	# 2 Check if the file exists...
	folderExists = os.path.exists(folderPath)	
	dirsearchFilePath = folderPath + "/" + domainName.strip()
	
	if folderExists:
		print("Found the " + folderPath + " file, so adding the folder: " + domainName)
		os.mkdir(dirsearchFilePath)
	else:
		print("else called creating RFB foler")
		# Folder doesnt exists so creating RFB_Results
		os.mkdir(folderPath)
		os.mkdir(dirsearchFilePath)
			
	extractedCodes = extractCodes(dirsearchFilePath)
	
	_200sLength = len(extractedCodes[0])
	_300sLength = len(extractedCodes[1])
	_400sLength = len(extractedCodes[2])
	_500sLength = len(extractedCodes[3])
	
	if _200sLength > 0:
		loopResponseUrlsAndAddToFile(dirsearchFilePath + "/200" + FILE_SUFFIX, extractedCodes[0])		
	if _300sLength > 0:
		loopResponseUrlsAndAddToFile(dirsearchFilePath + "/300" + FILE_SUFFIX, extractedCodes[1])
	if _400sLength > 0:
		loopResponseUrlsAndAddToFile(dirsearchFilePath + "/400" + FILE_SUFFIX, extractedCodes[2])
	if _500sLength > 0:
		loopResponseUrlsAndAddToFile(dirsearchFilePath + "/500" + FILE_SUFFIX, extractedCodes[3])

	endOfProgramReport.append([domainName.strip(), _200sLength, _300sLength, _400sLength, _500sLength])
	

# ////// Main function

def launch():
	print ("Running Scan and Attack")

	subDomsFileName = args.domainFile

	if not os.path.exists(subDomsFileName):
		print("Cannot find file: " + subDomsFileName + "\nExiting!")
		sys.exit()
	# If here a valid file name was entered... continuing
	
	sdf = open(subDomsFileName, 'r')
	
	for domain in sdf:
		print("Launching Dirsearch against: " + colored(domain.strip(), "yellow", attrs=["bold"]))
		
		httpsDomain = "https://" + domain.strip()
		outputFileName = domain.strip() + "_dirScanResult.txt"
		
		dirsearchCommand = "python3 /opt/WEB_APP_HACKING_TOOLS/discovery/dirsearch/dirsearch.py -E -u " + httpsDomain + " --plain-text-report " + outputFileName
		dirSearchExecutedSuccessfully = False
		
		try:
			sp.check_call(dirsearchCommand.split())
			dirSearchExecutedSuccessfully = True
			
		except sp.CalledProcessError:
			print("Dirsearch scan ran into an error")
		
		# Check if the dirsearch scan executed...
		if dirSearchExecutedSuccessfully:
			generateDirectories(outputFileName, domain) # Pass in the file that was just created
			
		print("\nEnd of loop...")
			
	sdf.close()
	
launch()

for i in endOfProgramReport:
	print("Report for " + colored(str(i[0]), "yellow", attrs=["bold"]) + " 200s: " + colored(str(i[1]), "green", attrs=["bold"]) + " 300s: " + colored(str(i[2]), "green", attrs=["bold"]) + " 400s: " + colored(str(i[3]), "green", attrs=["bold"]) + " 500s: " + colored(str(i[4]), "green", attrs=["bold"]))

	
	
	
	
	
	
	




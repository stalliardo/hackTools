#!/usr/bin/python3

import argparse
import sys
import os
from termcolor import colored
import subprocess as sp
#from progress bar import Bar
from progress.spinner import Spinner

parser = argparse.ArgumentParser()
parser.add_argument("attackMethod", help="Whether to scan for urls or just attack urls. s = scan and attack, a = attack only")


args = parser.parse_args()

# TODO - Create parent folder called RFB_Results
# TODO - Generate terminal output when running dirsearch
# TODO - implement a progress bar
# TODO - What happens on an iteration of the domain file when dirsearch returns no content

# TODO - Rethink script execution
	# Looking at the dirsearch results from deliveroo.co.uk raised a concern that what happens when lots of false positives are generated?
	# ie, liek loads of 403's or rdirects
# TODO - Create a new dirsearch scanner that will have the sole purpose of scanning domains, creating files ie for 200's, 300's, etc and generate a report ie 1000 200 response codes found
# TODO - Then review the report and decide which one seems like a good staring point for using with this tool
# TODO - So can remove the attacjMethod arg as this file will just be used for attacking
# TODO - Maybe add an arg for what type of attack ie, 403 bypass or 405 method tampering



def scanAndAttack():
	print ("Running Scan and Attack")
	# TODO - Get the user input for the file of subdomains
	subDomsFileName = input("Enter the name of the subdomain file: ")

	
	while not os.path.exists(subDomsFileName): # Loop until a valid file entered... How many times is this used? Does it need to be a function?
		print("No such file: " + subDomsFileName)
		subDomsFileName = input("Enter the name of the subdomain file: ")
	
	# If here a valid file name was entered... continuing
	
	sdf = open(subDomsFileName, 'r')
	
	
	for domain in sdf:
	
		print("Launching Dirsearch against: " + colored(domain.strip(), "yellow", attrs=["bold"]))
		
		#python3 /opt/WEB_APP_HACKING_TOOLS/discovery/dirsearch/dirsearch.py -E -u $1 --plain-text-report $2
		
		httpsDomain = "https://" + domain.strip()
		outputFileName = domain.strip() + "_dirScanResult.txt"
		
		
		dirsearchCommand = "python3 /opt/WEB_APP_HACKING_TOOLS/discovery/dirsearch/dirsearch.py -E -u " + httpsDomain + " --plain-text-report " + outputFileName
		
		#dirsearchCommand = "ls -la"
		#spinner = Spinner("Loading ")
		#while not dirSearchScanComplete:
			#spinner.next()
		
		
		try:
			sp.check_call(dirsearchCommand.split())
			print("under check_call")
		except sp.CalledProcessError:
			print("Dirsearch scan ran into an error")
		finally:
			print("\nScan finished")
			
			# Scan x complete, now check the length of the create file, if its 0 then what? Use another wordlist or should the word list be 

				
		
		
		
		
	sdf.close()
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def attackOnly():
	print("Running Attack only")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

attackMethod = args.attackMethod
if attackMethod == "s":
	scanAndAttack()
elif attackMethod == "a":
	attackOnly()
else:
	print(attackMethod + " is not a valid attack mode! \nExiting!")
	sys.exit()
	



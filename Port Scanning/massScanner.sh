#!/bin/bash

RED='\033[0;31m'
BLUE='\033[0;96m'
GREEN='\033[0;92m'
NC='\033[0m'

printf "\n -/-/-/-/-/-/-/- ${BLUE}Custom masscan usage by ${RED}TheQuacken${NC} -/-/-/-/-/-/-/- \n\n"

ipFile=$1

if test -z "$1"

	then 
		echo "Enter the path to the ip file"
	fi
	
printf "masscan scanning complete, loading checkForVulnerablePorts.sh"

masscan -iL $ipFile --max-rate=1800 -v -p1-65535 -oG massScanOutput.txt

/root/Documents/custom-tools/portScanning/./checkForVulnerablePorts.sh massScanOutput.txt

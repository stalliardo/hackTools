#!/bin/bash

RED='\033[0;31m'
BLUE='\033[0;96m'
GREEN='\033[0;92m'
NC='\033[0m'

printf "\n -/-/-/-/-/-/-/- ${BLUE}Custom port scanner by ${RED}TheQuacken${NC} -/-/-/-/-/-/-/- \n\n"

portFile=$1

if test -z "$1"
then 
	echo "You need to provide a file with ports in"
	exit
fi

vulnerablePorts=(20 21 22 23 25 110 135 137 139 389 636 1025 1433 1434 3306 4333 5432)

for i in "${vulnerablePorts[@]}"
	
do
	echo "Scanning for port $i"
	result=$(cat $portFile | grep -w "$i/open" )
	if [ $? -eq 0 ];then
	
		printf "${GREEN}Port $result found${NC}\n"
		
		fi	
	
done

printf "\n -/-/-/-/-/-/-/- ${GREEN}Scan complete ${NC} -/-/-/-/-/-/-/- \n\n"

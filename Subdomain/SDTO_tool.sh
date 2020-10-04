#!/bin/bash
# Program name: pingscript.sh
#date

RED='\033[0;31m'
GREEN='\033[0;92m'
NC='\033[0m' # no colour

printf "\n\n************** ${RED}Subdomain enumeration tool from ${GREEN}the quacken${NC} **************"

if test -z "$1" 

then
      echo "Please provide domian name"
      exit
fi

printf "\n\n************** ${RED}Unique ips will be added to ${GREEN}generatedIps.txt${NC} **************\n"

domainToScan=$1

liveDomainsTmp=tmpFoundFile
outputFile=generatedIps.txt

amass enum -passive -d $domainToScan >> amassScanOutput.txt

# This is what reads the output of the amass scan
cat amassScanOutput.txt |  while read output
do
    ping -c 1 -w 1 "$output" > /dev/null
    if [ $? -eq 0 ]; then     # $? checks the exit status of the previous command 0 is true 1 is false
    echo "node $output is up"
    echo "$output" >> $liveDomainsTmp
    else
    echo "node $output is down"
    fi
    echo ""
done

printf "************ RESOLVING LIVE DOMAINS TO IP ADDRESS ************\n\n"


cat $liveDomainsTmp | while read domain # Loops through only the "live" domains

do 
	ip=$(getent ahostsv4 $domain | awk '{print $1}' | head -1) >> fileToBeSorted # generates a file of ips, but also want the domain and ip in an additional file
	echo $ip >> fileToBeSorted
	echo "$domain has ip address: $ip" >> domainAndIp.txt
	printf "************ Resolved $domain ************\n"
done

sort fileToBeSorted | uniq > $outputFile

rm fileToBeSorted

printf "\n************** Temporay file removed! **************\n\n"

printf "\n************** Duplicate ips have been removed! Files: $outputFile and dominAndIp.txt have been created! **************\n\n"

cat domainAndIp.txt | while read line

do 

	sed 's/has.*//g' domainAndIp.txt > striped_domains.txt
	
done

printf "Domains extracted! striped_domains.txt file created!\n"

printf "Checking for NXDOMAIN in striped_domains.txt\n"

cat striped_domains.txt | while read domain

do

	dig -t A $domain | grep NXDOMAIN
	
	if [ $? -eq 0 ];then
		echo "NXDOMAIN returned from dig command found in domain:  $domain"
		echo $domain >> foundNXDOMAINRecords.txt
	fi
	
done

printf "${GREEN}SDTO script execution complete\n"

rm $liveDomainsTmp

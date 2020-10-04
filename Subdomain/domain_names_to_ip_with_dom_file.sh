#!/bin/bash
# Program name: pingscript.sh
#date

printf "\n\n************** Enter domain list file as first arg and output file name as second arg! **************\n\n"

if test -z "$1" 

then
      echo "Please provide a file containing the domain names."
      exit
fi

if test -z "$2" 

then
      echo "Please specify an outputfile name"
      exit
fi

liveDomainsTmp=tmpFoundFile
outputFile=$2


cat $1 |  while read output
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

printf "\n************** Script execution complete, Duplicate ips have been removed! Files: $outputFile and dominAndIp.txt have been created! **************\n\n"

rm $liveDomainsTmp

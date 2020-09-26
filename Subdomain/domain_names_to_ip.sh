#!/bin/bash

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
    ping -c 1 "$output" > /dev/null
    if [ $? -eq 0 ]; then     # $? checks the exit status of the previous command 0 is true 1 is false
    echo "node $output is up"
    echo "$output" >> $liveDomainsTmp
    else
    echo "node $output is down"
    fi
    echo ""
done

printf "************ RESOLVING LIVE DOMAINS TO IP ADDRESS ************\n\n"


cat $liveDomainsTmp | while read domain

do 
	getent ahostsv4 $domain | awk '{print $1}' | head -1 >> fileToBeSorted
	printf "************ Resolved $domain ************\n"
done

sort fileToBeSorted | uniq > $outputFile

printf "\n************** Script execution complete, Duplicate ips have been removed! File: $outputFile created! **************\n\n"


# What about duplicate ips??

rm $liveDomainsTmp



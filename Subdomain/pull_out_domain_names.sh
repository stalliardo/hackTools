#!/bin/bash
# This is a simple script to extract the domains names from a file containing strings in the following format "someDomain.com has the ip address <some ip address>"

fileToStrip=$1

cat $fileToStrip | while read line

do 

	sed 's/has.*//g' $fileToStrip > striped_domains.txt
	
done

printf "Domains extracted! striped_domains.txt file created!\n"

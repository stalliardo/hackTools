#!/bin/bash

printf "\n\n* * * DOM Sink Scanner * * *\n\n"

fileToScan=$1

sinkWords=("location" "location.test" "location.hostname" "location.href" "location.pathname" "location.search" "location.protocol" "location.assign()" "location.replace()" "open()" "domElem.srcdoc" "XMLHttpRequest.open()" "XMLHttpRequest.send()" "jQuery.ajax()" "$.ajax()")

for i in "${sinkWords[@]}"
do
	# Loop over each and use grep to search the given file
	printf "\n\n********** Searching $fileToScan for $i **********\n\n"
	cat $fileToScan | grep -n $i
done

printf "\n\n* * * Script execution complete * * *\n\n"




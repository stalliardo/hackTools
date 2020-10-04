#!/bin/bash

file=$1

cat $file | while read domain

do

	dig -t A $domain | grep NXDOMAIN
	
	if [ $? -eq 0 ];then
		echo "NXDOMAIN returned from dig command found in domain:  $domain"
		echo $domain >> foundNXDOMAINRecords.txt
		
	else 
		echo "No NXDOMAIN returned from $domain"
	fi
	
done

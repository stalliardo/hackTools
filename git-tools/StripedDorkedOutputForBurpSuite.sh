#!/bin/bash

query=$1

if test -z $1
	then 
		printf "\nEnter a query string such as a domain name\n\n"
		exit
	fi

./Gdorklinks.sh $query >> tmpfile.txt


# get the string required by burp

sed -e 's/https:\/\/github.com\/search?q=//g' tmpfile.txt >> stripedfile.txt

# remove unnecassary words

cat stripedfile.txt | grep '%22' > query_list_for_burp.txt

rm tmpfile.txt
rm stripedfile.txt

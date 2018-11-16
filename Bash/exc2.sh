#!/bin/bash

RETURN_CODE=$?
num=5

#Print the number 5 times
for (( i=1; i<=num; i++ ))
do
	
	#print the number 5 times on the line
	for (( j=1; j<num; j++ ))
	do
		echo -n $i
	done
	#Starts a new line
	echo
done
exit 0

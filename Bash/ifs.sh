#!/bin/bash

VAR1=$1
VAR2=$2

if [ $VAR1 -gt $VAR2 ]
then
	echo "Var1 is greater than var 2"

elif [ $VAR1 -lt $VAR2 ]
then
	echo "Var1 is less than var 2"

elif [ $VAR1 -eq $VAR2 ]
then
	echo "Var1 is equal to var 2"
fi

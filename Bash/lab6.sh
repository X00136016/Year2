#!/bin/bash

touch file2  

if [ -e file1 ] && [ -e file2 ]
then
	echo "file 1 & file2 exists "

elif [ -e file1 ] 
then
	echo "Only File 1 exists"

elif [ -e file2 ]
then
	echo "Only file 2 exists"
fi

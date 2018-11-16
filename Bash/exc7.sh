#!/bin/bash

for i in $( ls *.txt); do
	#echo $i
	du $i
done


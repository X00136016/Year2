#!/bin/bash
touch ss.txt sss.txt

for i in *.txt
do
	du $i
done

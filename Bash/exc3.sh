#!/bin/bash

Dub=Dublin2017-
touch s.jpg ss.jpg sss.jpg

if [ -e /tmp/bckup ]
then
	echo "File already exists"

else
	echo "File doesnt exist yet but is being created.."
fi

mkdir /tmp/bckup

for i in *.jpg
do
	mv $i /tmp/bckup/$Dub$i
done



#!/bin/bash

#displays number of subdirectories in the current folder
ls -d -- */ | wc -w

#Displays number of files in a directory
find *.* | wc -w

#Displays total amount of space used
df --total /home/student

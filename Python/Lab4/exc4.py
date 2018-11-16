#!/usr/bin/env python3
import subprocess

#Part (A)
#showing the content of the /etc/passwd directory
def cat_func():
    cat="cat"
    cat_arg="/etc/passwd"
    print("The contents are as follows  : ")
    subprocess.call([cat,cat_arg])

#Part (B)
#Listing the content of the /tmp directory
def tmp_func():
    ls="ls"
    ls_arg="/tmp"
    print("The contents of /tmp are : ")
    subprocess.call([ls,ls_arg])


#Part (C)
#List the running processes

#Set variable to command
def ps_func():
    cmd="ps"
    # Call process
    subprocess.call([cmd])

#Part(D)
def diskcall():
    #Set Variable to command
    disk="du"
    subprocess.call([disk])


def main():
    diskcall()
    ps_func()
    tmp_func()
    cat_func()

main()



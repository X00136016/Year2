#!/usr/bin/env python3 

import subprocess

#Finding the routing Kernel
def route():
    route="route"
    route_arg="-n"
    subprocess.call([route,route_arg])

#Finding the disk usage of the /tmp directory
def tmp():
    diskusage="df"
    tmp="/tmp"
    subprocess.call([diskusage,tmp])

#Finding empty files on the /tmp directory
def emptmp():
    find="find"
    tmp="/tmp"
    emp="-empty -type f"
    subprocess.call(['find','/tmp','-empty','-type','f'])

def ps():
    ps="ps"
    arg="-u"
    root="root"
    subprocess.call(['ps','-u','root'])

#Calling all functions
def main():
    #route()
    #tmp()
    #emptmp()
    ps()

if __name__=="__main__":
    main()

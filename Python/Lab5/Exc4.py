#!/usr/bin/env python3

def find_str():
    myString="The script is not poor";
    
    # searchg for not
    search_not = "not";
    #resturns the index if found or -1 if not
    res1=myString.find(search_not)
    
    # search for poor
    search_poor = "poor";
    #resturns the index if found or -1 if not
    res2=myString.find(search_poor)
    
    #if both arent found then return the original string
    if res1 ==-1 and res2==-1:
        return(myString)
    #if res1 is first 
    elif res1 < res2:
        # replace not with very
        ans1 = myString.replace(search_not,"very")
        
        
        #replace poor with good
        print (ans1.replace(search_poor,"good"))
    elif res1 > res2:
        print (myString)

         


def main():
    find_str()

main()

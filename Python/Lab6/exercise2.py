
#Read number from the keyboard
def readFromKb():
    #try to convert it to an integer
    num=int(input("Enter a number bwtween 1 and 20 ->"))
    return num

def setupDict(size):
    #initial the dictionary
    mydict = {}
    #loop through and add to the dictionary
    for i in range(1,size):
        mydict.update({i:i*i})
        #print("Dict ", mydict[i])
    
    #print(mydict)
    return mydict
    
#check its a valid else error
def isValid(num, mydict):
    print("Num is ", num)
    print ("Answer ",mydict[num])


def main():
    mydict = setupDict(21)
    num = readFromKb()
    isValid(num,mydict)

main()
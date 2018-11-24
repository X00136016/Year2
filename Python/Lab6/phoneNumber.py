#!/usr/bin/env python3

#Checking the correct length
def isCorrectLength(num):
    #if length is equal to 13 its true or else its false
    if len(num)==13:
        return True
    else:
        return False

#Checks the character at the index is equal to dash.
def isDash(num,index):
    if num[index]=='-':
        return True
    else:
        return False

#Counts the next 3 characters are number starting at index.
def threeNumbers(num,index):
    for i in range(index,index+2):
        print ("checking", i, num[i])
        if not num[i].isdecimal():
            return False
        return True


#Starting at index the next four characters are numbers.
def fourNumbers(num,index):
    for i in range(index,index+3):
        if not num[i].isdecimal():
            return False
        return True
        


def main():
    #Asks for input
    print("Enter a valid number")
    num=input()
    
    #Dislays result
    print("You entered",num)
    test1 = isCorrectLength(num)    

    #Checks the character 5 is a dash (index 4)
    test2 = isDash(num,4)
    
    test3 = isDash(num,8)
    
    test4= threeNumbers(num,5)

    test5 = fourNumbers(num,9)
   
   
    #if all tests are true its valid or invalid
    if test1 and test2 and test3 and test4 and test5:
        print("This a valid Phone Number")
    else:
        print("This is an invalid number")
main()

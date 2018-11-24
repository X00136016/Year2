import re

#Read from the keyboard
def readFromKB():
    email = input("Enter an email address ->")
    return email

#Validate the email and print the result
def validateEmail(email):
    if re.match("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|ie|co.uk)", email):
        print( email, " is valid")
    else:
        print(email, " is not valid")

def main():
    email=readFromKB()
    validateEmail(email)

main()
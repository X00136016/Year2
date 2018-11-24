import re

#Read from the keyboard
def readFromKB():
    sentence = input("Enter a hyphen separated string ->")
    return sentence

#Split and sort the words
def splitAndSort(sentence):
    #Split on the dashes
    wordList = sentence.split('-')
    #Sort the word list
    wordList.sort()

    return wordList


#Add hyphens and print the answer
def replaceHyphens(sentence):
    separator = '/'
    #Join the words with a slash
    print(separator.join(sentence))


def main():
    sentence = readFromKB()
    sortedSentence = splitAndSort(sentence)
    print("Sorted is ",sortedSentence)
    replaceHyphens(sortedSentence)

main()
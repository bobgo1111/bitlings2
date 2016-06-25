#This is a program word countinator 2.0 by Caleb and Curtis .6/19/16


import os.path, pprint

def theAsker():
    theFilename = input("Give us the preciousss! We wants it! Give us the filename!")
    if os.path.isfile(theFilename) == True:
         print("good job thats a legit filename")
    else:
        print("That is no true filename!!")
        while os.path.isfile(theFilename) == False:
            theFilename = input("Give a real filename")
        print("thats a legit filename!")
    return theFilename

theFile = theAsker()
theFilehandle = open(theFile, "r")
lines = theFilehandle.readlines()
print("this is what your file says: " + str(lines))

total = 0

allWords = []

for line in lines:
    words = line.split()
    allWords.extend(words)

copyOfAllWords = []

def fixer(word):
    emptylist = []
    word = word.strip("'")
    for character in word:
        if character >= "A":
            emptylist.append(character)
    return ''.join(emptylist)

for t in allWords:
    if t >= "A":
        t = fixer(t)
        copyOfAllWords.append(t)

print("these are the number of lines: " + str(len(lines)))

copyOfAllWords.sort()

allWordsDeduped = {}

for x in lines:
    total = total + len(x.split())

print("there are " + str(total) + " words in this document")

for w in copyOfAllWords:
    allWordsDeduped[w] = allWordsDeduped.get(w, 0) + 1

pprint.pprint(allWordsDeduped)

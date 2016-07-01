#This is a program word countinator 2.0 by Caleb and Curtis .6/19/16


import os.path, pprint

def filenameAsker():
    theFilename = input("Please type a file name: ")
    if os.path.isfile(theFilename) == True:
         print("good job thats a legit filename")
    else:
        print("That is no true filename!!")
        while os.path.isfile(theFilename) == False:
            theFilename = input("Give a real filename")
        print("thats a legit filename!")
    return theFilename


def wordCleaner(word):
    """
    Takes out all punctuation and number characters from a word.

    :param word: The word to clean
    :return: The cleaned word
    """
    emptylist = []
    word = word.strip("'")
    for character in word:
        if character >= "A":
            emptylist.append(character)
    return ''.join(emptylist)

def readFile(fileName):
    """
    This function reads a file and returns a list of all its lines.

    :param fileName: The name of the file to open
    :return: a list of lines from the file
    """
    theFilehandle = open(fileName, "r")
    lines = theFilehandle.readlines()
    print("this is what your file says: " + str(lines))
    theFilehandle.close()
    return lines

def linesToWords(lines):
    allWords = []
    for line in lines:
        words = line.split()
        allWords.extend(words)
    return allWords

def main():
    theFileName = filenameAsker()
    lines = readFile(theFileName)
    allWords = linesToWords(lines)

    copyOfAllWords = [wordCleaner(t) for t in allWords if t >= "A"]

    print("these are the number of lines: " + str(len(lines)))

    copyOfAllWords.sort()

    allWordsDeduped = {}

    total = 0

    for x in lines:
        total = total + len(x.split())

    print("there are " + str(total) + " words in this document")

    for w in copyOfAllWords:
        allWordsDeduped[w] = allWordsDeduped.get(w, 0) + 1

    print("This is a list of the words in your document (below) and how many of each word there are:")
    pprint.pprint(allWordsDeduped)

if __name__ == "__main__":
    main()

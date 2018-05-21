import sys
import json
import random
import string
import os.path
import tokenize
from pathlib2 import Path


def init():
    data = None
    print("Enter 'help' for help and 'exit' to exit program...")
    # Create recent file if it does not exist
    recentFile = Path(".recent")
    if not recentFile.is_file():
        r = open(".recent", "w")
        r.close()
    # Create dictionary if it does not exist
    dictFile = Path("dict.json")
    if not dictFile.is_file():
        print("Initializing new dictionary...")
        writeToFile({})
        # If the dictionary is new and the '.recent' file already exists, then
        # the '.recent' file needs to be reset
        f = open(".recent", "w")
        f.truncate()
        f.close()
    # Get the contents of the dictionary file
    with open("dict.json") as json_file:
        data = json.load(json_file)
        if not data or data == None:
            print("Dictionary is empty...")
    return data


def tokenize(input):
    arr = []
    tempString = ""
    for i in input:
        if i == " ":
            arr.append(tempString)
            tempString = ""
        else:
            tempString += i
    arr.append(tempString)
    return arr


def search(data, search):
    # Searched item was not found
    if lookup(data, search) == False:
        print "Item not found in dictionary"
        return
    # Searched item was found
    showWord(data, search)


def add(data, word):
    # Word already exists
    if lookup(data, word):
        answer = raw_input("Word found! Add Definition? (y/n): ").lower()
        if answer == "y":
            definition = raw_input("Enter definition: ")
            # Create unique ID
            ID = None
            while(1):
                ID = genId()
                if ID not in data[word]:
                    break
            # Add definition
            data[word].update({
                ID: definition
            })
            writeToFile(data)
            return
        else:
            return
    else:
        data[word] = {}
        definition = raw_input("Enter definition: ")
        data[word].update({
            genId(): definition
        })
        writeToFile(data)
        updateRecent(word)


def remove(data, operation, word):
    if operation == "word":
        # Word does not exist
        if not lookup(data, word):
            print("Word not found...")
            return
        # Word has been found
        del data[word]
        writeToFile(data)
    elif operation == "definition":
        # Word does not exist
        if not lookup(data, word):
            print("Word not found...")
            return
        # Word has been found
        definitions = data[word]
        showWord(data, word)
        id = None
        while (1):
            id = raw_input("Enter definition ID: ")
            if id not in definitions:
                print "Invalid input..."
            else:
                break
        del definitions[id]
        data[word] = definitions
        writeToFile(data)
    else:
        print "Invalid input..."


# View most recently used words
def recent():
    content = [line.rstrip('\n') for line in open(".recent")]
    for i in content[::-1]:
        print i


# Print the help
def help():
    f = open(".help", "r")
    print f.read()


# Safely get integer input from user
def getInt(printStatement):
    try:
        val = input(printStatement)
    # Not an integer
    except NameError:
        print "Invalid Input\n"
        return -999
    # Error check characters such as '^[]'
    except SyntaxError:
        print "Invalid Input\n"
        return -999
    return val


# Shows information for a given word in dict
def showWord(data, word):
    numDefs = len(data[word])
    print "(%s): %d definition(s)" % (word, numDefs)
    defs = data[word]
    for i in defs:
        print "[%s] --- %s" % (i, defs[i])


# update recent word list
def updateRecent(word):
    content = [line.rstrip('\n') for line in open(".recent")]
    if len(content) >= 15:
        content.pop(0)
        content.append(word)
    else:
        content.append(word)
    # open file as write to clear it
    f = open(".recent", "w")
    f.truncate()
    for i in content:
        f.write("%s\n" % i)
    f.close()


# Search for word via keyword in definitions
def near(data, keyword):
    for word in data:
        key = data[word]
        for defi in key:
            if keyword in key[defi]:
                showWord(data, word)
                break


def genId():
    id = ""
    for i in [1,2,3,4]:
        id = id + random.choice(string.letters).lower()
    return str(id)


# Primary 'save' function
def writeToFile(data):
    with open("dict.json", "w") as outfile:
        json.dump(data, outfile)


# Returns true if word is within dictionary
def lookup(data, word):
    if word in data:
        return True
    else:
        return False


# Gracefully print error message and quit app
def error(errorMessage):
    print errorMessage + "\n Exiting app..."
    sys.exit(-1)

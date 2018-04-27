import json
import os.path
import sys
import definitions as de
from pathlib2 import Path
import tokenize

def init():
    data = None
    dictFile = Path("dict.json")
    if not dictFile.is_file():
        print("Initializing new dictionary...")
        # Create file if it does not exist
        writeToFile({})
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
            data[word].update({
                str(len(data[word]) + 1): definition
            })
            writeToFile(data)

            return
        else:
            return
    else:
        data[word] = {}
        definition = raw_input("Enter definition: ")
        data[word].update({
            str(len(data[word]) + 1): definition
        })
        writeToFile(data)


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
        index = None
        while (1):
            index = raw_input("Enter definition number: ")
            if index not in definitions:
                print "Invalid input..."
            else:
                break
        del definitions[index]
        data[word] = definitions
        writeToFile(data)
    else:
        print "Invalid input..."


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


# Shows information for a given word dict
def showWord(data, word):
    numDefs = len(data[word])
    print "%s: %d definition(s)" % (word, numDefs)
    count = 1
    defs = data[word]
    for i in defs:
        print "[%s] %s" % (count, defs[i])
        count = count + 1


# Print the help
def help():
    pass


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

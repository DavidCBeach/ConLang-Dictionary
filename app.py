import json
import os.path
import sys
from pathlib2 import Path


def main():
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
    # Main function loop
    while (1):
        print "Enter a number for an operation..."
        operation = getInt("(1)Search, (2)Add, (3)Remove, (4)exit: ")
        # Run operation
        if (operation == 1):
            search(data)
        elif (operation == 2):
            add(data)
        elif (operation == 3):
            remove(data)
        elif (operation == 4):
            return
        else:
            print "Invalid input...\n"


def search(data):
    print "\n"
    search = raw_input("Search for: ")
    # Searched item was not found
    if lookup(data, search) == False:
        print "Item not found in dictionary\n"
        return
    # Searched item was found
    showWord(data, search)


def add(data):
    print "\n"
    word = raw_input("Add word: ")
    # Word already exists
    if lookup(data, word):
        answer = raw_input("Word found! Add Definition? (y/n): ").lower()
        if answer == "y":
            definition = raw_input("Enter definition: ")
            data[word].update({
                str(len(data[word]) + 1): definition
            })
            writeToFile(data)
            print"\n"
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
    print"\n"


def remove(data):
    operation = getInt("Remove (1)Word, (2)Definition, (3)Cancel: ")
    if operation == 1:
        word = raw_input("Remove word: ")
        # Word does not exist
        if not lookup(data, word):
            print("Word not found...\n")
            return
        # Word has been found
        del data[word]
        writeToFile(data)
    elif operation == 2:
        word = raw_input("Enter word: ")
        # Word does not exist
        if not lookup(data, word):
            print("Word not found...\n")
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
        print "Invalid input...\n"


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
    print "\n"


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


if __name__ == "__main__":
    main()

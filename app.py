import json
import os.path
import sys
from pathlib2 import Path


def main():
    data = None
    dictFile = Path("dict.json")
    if not dictFile.is_file():
        error("Could not find dictionary file")
    with open('dict.json') as json_file:
        data = json.load(json_file)
        if not data or data == None:
            error("No data found within dictionary file")
    # Main function loop
    while (1):
        print "Enter a number for an operation..."
        try:
            operation = input("(1)Search, (2)Add, (3)Remove, (4)exit: ")
        # Not an integer
        except NameError:
            print "Invalid Input\n"
            continue
        # Error check characters such as '^[]'
        except SyntaxError:
            print "Invalid Input\n"
            continue
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
    search = raw_input("Search for: ")
    # Searched item was not found
    if lookup(data, search) == False:
        print "Item not found in dictionary\n"
        return
    # Searched item was found
    word = data[search]
    numDefs = len(word)
    print "\n"
    print "%s: %d definition(s)" % (search, numDefs)
    count = 01
    for i in word:
        print "[%s] %s" % (count, word[i])
        count = count + 1
    print "\n"


def add(data):
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
            return
        else:
            return
    print"\n"


def remove():
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


if __name__ == "__main__":
    main()

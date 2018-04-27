import json
import os.path
import os
import sys
import definitions as de
from pathlib2 import Path


def main():
    data = de.init()
    while (1):
        input = raw_input("> ")
        tokens = de.tokenize(input)
        length = len(tokens)
        check = tokens[0].lower()
        # Search for a word
        if check == "search":
            de.search(data, tokens[1])
        # Add a word or definition
        elif check == "add":
            if length < 2:
                print "Invalid input..."
                continue
            de.add(data, tokens[1])
        # Remove word or definition
        elif check == "remove":
            if length != 3:
                print "Invalid input..."
                continue
            de.remove(data, tokens[1].lower(), tokens[2])
        elif check == "help":
            if length > 1:
                print "Invalid input..."
                continue
            de.help();
        # Clear terminal
        elif check == "clear":
            if length > 1:
                print "Invalid input..."
                continue
            os.system('cls' if os.name == 'nt' else 'clear')
        # Exit out of our app
        elif check == "exit":
            return


if __name__ == "__main__":
    main()

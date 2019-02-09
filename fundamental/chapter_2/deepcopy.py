# Python Version 3
# File Name : deepcopy.py

import copy, sys

def filetolist(filename):
    templist = []
    try:
        file = open(filename)
        for line in file:
            templist.append(line)
    
    except IOError as e:
        print(e)
        sys.exit(1)

    return templist

def printlist(li):
    for e in li:
        print(e, end='')


def main():
    phonebook = filetolist("data.txt")

    sortedlist = sorted(copy.deepcopy(phonebook))

    print("\nSebelum diurutkan\t: ")
    printlist(phonebook)

    print("\n\nSesudah diurutkan\t: ")
    printlist(sortedlist)

if __name__ == "__main__":
    main()

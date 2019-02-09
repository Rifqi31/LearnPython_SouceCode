# Python Version 3
# File Name : exception_statement.py

import sys

def main():

    try:
        filename = "datafile.txt"

        # membuka file
        openfile = open(filename)
        
        # membaca file
        for line in openfile("datafile.txt"):
            print(line, end='')

        # menutup file
        openfile.close()
    
    except IOError:
        print("File '%s' tidak ditemukan." % filename)
        sys.exit()

if __name__ == "__main__":
    main()

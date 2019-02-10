#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : get_dictio.py


def CallBook(phoneNumber):
    contact_person = {
        123: "Sabrina",
        222: "Isabella",
        313: "Rifqi"
    }

    print("Hi %s " % contact_person.get(phoneNumber, "there"))


def main():
    """
        Python Tricks Today:
        how to use get() for dictionary
    """
    inputValue = int(input("insert phone number\t: "))

    # show the result
    CallBook(inputValue)


if __name__ == "__main__":
    main()

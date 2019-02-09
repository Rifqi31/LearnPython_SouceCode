#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_7.py


def main():
    """
        Basic Exercise Part 1
        Write a Python program to accept a filename
        from the user and print the extension of that.
    """

    filename = input("insert file name\t: ")
    file_ext = filename.split(".")

    print("this file have " + repr(file_ext[-1]) + " an extension")


if __name__ == "__main__":
    main()

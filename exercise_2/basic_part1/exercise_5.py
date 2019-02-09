#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_5.py


def main():
    """
        Basic Exercise Part 1
        Write a Python program which accepts the user's first
        and last name and print them in reverse order
        with a space between them.
    """

    first_name = input("insert first name\t: ")
    last_name = input("insert last name\t: ")

    print(last_name + " " + first_name)


if __name__ == "__main__":
    main()

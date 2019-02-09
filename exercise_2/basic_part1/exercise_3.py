#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_3.py

import datetime


def main():
    """
        Basic Exercise Part 1
        Write a Python program to display the current date and time.
    """
    now = datetime.datetime.now()
    print("Current date and time\t: ")
    print(now.strftime("%Y-%M-%D %H:%M:%S"))


if __name__ == "__main__":
    main()

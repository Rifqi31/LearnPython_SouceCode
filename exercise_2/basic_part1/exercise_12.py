#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_12.py

import calendar


def main():
    """
        Basic Exercise Part 12
        Write a Python program
        to print the calendar of a given month and year.
    """

    in_year = int(input("input the year\t: "))
    in_month = int(input("input the month\t: "))

    result = calendar.month(in_year, in_month)

    # show the result
    print(result)


if __name__ == "__main__":
    main()

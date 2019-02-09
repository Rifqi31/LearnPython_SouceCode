#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_14.py

from datetime import date


def main():
    """
        Basic Exercise Part 14
        Write a Python program to calculate number of days between two dates.
    """
    dt1 = date(2014, 7, 2)
    dt2 = date(2014, 7, 11)

    delta = dt2 - dt1

    print(delta.days)


if __name__ == "__main__":
    main()

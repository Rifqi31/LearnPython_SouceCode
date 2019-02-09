#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_10.py

def main():
    """
        Basic Exercise Part 10
        Write a Python program that accepts an integer (n)
        and computes the value of n+nn+nnn.
    """
    # example value n is 5
    n = 5

    # first make string type first
    secondval = str(n) + str(n)
    thirdval = str(n) + str(n) + str(n)

    # print(secondval)
    # print(thirdval)

    # and the convert into integer
    new_secondval = int(secondval)
    new_thirdval = int(thirdval)

    # n + nn + nnn
    result = n + new_secondval + new_thirdval

    print(result)


if __name__ == "__main__":
    main()

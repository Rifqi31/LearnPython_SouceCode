#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_6.py


def main():
    """
        Write a Python program which accepts
        a sequence of comma-separated numbers
        from user and generate a list and a tuple with those numbers.
    """

    insertNumber = input("insert those numbers with comma separated\t: ")

    datalist = insertNumber.split(",")
    datatuple = tuple(datalist)

    print('List\t: ', datalist)
    print('Tuple\t: ', datatuple)


if __name__ == "__main__":
    main()

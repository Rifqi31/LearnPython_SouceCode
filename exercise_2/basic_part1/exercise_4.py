#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : exercise_4.py

import math


def main():
    """
        Basic Exercise Part 1
        Write a Python program which accepts the radius
        of a circle from the user and compute the area.
    """

    radius = float(input("insert radius numbers\t: "))

    area_of_rad = math.pi * math.pow(radius, 2)

    print(area_of_rad)


if __name__ == "__main__":
    main()

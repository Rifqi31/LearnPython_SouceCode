#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : merge_2dictio.py


def main():
    """
        How to merging two dictionary
    """
    data1 = {"A": 1, "B": 2}
    data2 = {"D": 4, "C": 3}

    mergedata = {**data1, **data2}

    # show the result
    print(mergedata)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : while_example_4.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Perulangan
        Statement While
    """

    # melakukan perulangan
    nCounter = 'a'
    while nCounter <= 'k':
        print("%c: Hello World" % nCounter)
        nCounter = chr(ord(nCounter) + 1)


if __name__ == "__main__":
    main()

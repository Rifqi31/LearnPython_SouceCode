#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : while_example_2.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Perulangan
        Statement While
    """

    # menentukan jumlah perulangan oleh user input
    n = int(input("masukkan jumlah perulangan\t: "))

    i = 1
    while i <= n:
        print(i)
        i += 1


if __name__ == "__main__":
    main()

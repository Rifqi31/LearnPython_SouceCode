#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: for_example_chr.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Perulangan
        Statement for
    """

    # menggunakan for untuk indeks karakter
    for nRead in range(ord('a'), ord('e')):
        print("%c: Hello World!" % chr(nRead))


if __name__ == "__main__":
    main()

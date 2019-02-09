#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : if_2case_else.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk dua kasus
    """

    # input untuk tipe integer
    bilangan = int(input("masukkan bilangan bulat\t: "))

    # membuat bilangan genap atau ganjil
    if bilangan % 2 == 0:
        print("%d adalah bilangan genap" % bilangan)
    else:
        print("%d adalah bilangan ganjil" % bilangan)


if __name__ == "__main__":
    main()

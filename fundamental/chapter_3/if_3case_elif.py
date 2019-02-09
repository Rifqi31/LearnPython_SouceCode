#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : if_3case_elif.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk tiga kasus atau lebih
    """

    # input user untuk tipe data integer
    xnumber = int(input("masukkan bilangan bulat\t: "))

    # memerikan nilai xnumber
    if xnumber == 0:
        print("%d adalah bilangan nol" % xnumber)
    elif xnumber > 0:
        print("%d adalah bilangan positif" % xnumber)
    else:
        print("%d adalah bilangan negatif" % xnumber)


if __name__ == "__main__":
    main()

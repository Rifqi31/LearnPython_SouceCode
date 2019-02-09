#!usr/bin/python3
# -*- coding: utf-8 -*-
############################################
# File Name : if_1case.py
############################################


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk satu kasus
    """

    bilangan = int(input("masukkan bilangan bulat\t: "))

    # memastikan bilangan genap atau tidak
    if bilangan % 2 == 0:
        print("%d adalah bilangan genap" % bilangan)


if __name__ == "__main__":
    main()

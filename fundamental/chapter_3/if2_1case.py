#!usr/bin/python3
# -*- coding: utf-8 -*-
############################################
# File Name : if2_1case.py
############################################


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk satu kasus
    """

    # membuat tuple
    namahari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")

    # membuat prompt untuk input data string
    inputhari = input("masukkan nama hari\t: ")

    # perintah if dengan dua ekspresi
    if inputhari.lower() == namahari[5] or inputhari.lower() == namahari[6]:
        print("%s adalah hari libur" % inputhari)


if __name__ == "__main__":
    main()

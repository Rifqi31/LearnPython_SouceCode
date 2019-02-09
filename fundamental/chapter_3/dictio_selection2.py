#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : dictio_selection2.py

# mendefinisikan fungsi tambah


def tambah(nilai1, nilai2):
    return nilai1 + nilai2

# mendefinisikan fungsi kurang


def kurang(nilai1, nilai2):
    return nilai1 - nilai2

# mendefinisikan fungsi kali


def kali(nilai1, nilai2):
    return nilai1 * nilai2

# mendefinisikan fungsi bagi


def bagi(nilai1, nilai2):
    return nilai1 / nilai2


def main():
    """
        Bab Statement Kontol
        Bagian Struktur Pemilihan
        Menggunakan Dictionary untuk melakukan pemilihan
    """

    nilai1 = float(input("masukkan bilangan ke-1\t: "))
    nilai2 = float(input("masukkan bilangan ke-2\t: "))
    operator = input("masukkan operator\t: ")

    # membuat dictionary yang nilainya berupa fungso
    opr_dictio = {
        '+': tambah(nilai1, nilai2),
        '-': kurang(nilai1, nilai2),
        '*': kali(nilai1, nilai2),
        'x': kali(nilai1, nilai2),
        '/': bagi(nilai1, nilai2),
        ':': bagi(nilai1, nilai2)
    }

    print("\n%f %s %f = %f" % (nilai1, operator, nilai2, opr_dictio[operator]))


if __name__ == "__main__":
    main()

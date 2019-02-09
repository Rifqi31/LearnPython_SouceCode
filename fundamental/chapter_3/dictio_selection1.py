#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : dictio_selection1.py


def main():
    """
        Bab Statement Kontol
        Bagian Struktur Pemilihan
        Menggunakan Dictionary untuk melakukan pemilihan
    """

    # membuat dictionary
    namahari = {
        1: "Minggu",
        2: "Senin",
        3: "Selasa",
        4: "Rabu",
        5: "Kamis",
        6: "Jumat",
        7: "Sabtu"
    }

    # input tipe integer
    nohari = int(input("masukkan nomer hari\t: "))

    print("Hari ke-%d adalah hari %s" % (nohari, namahari[nohari]))


if __name__ == "__main__":
    main()

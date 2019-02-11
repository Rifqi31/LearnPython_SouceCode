#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : for_example_list2.py

def main():
    """
        Bab Statement Kontrol
        Bagian Statement Perulangan
        Statement for
    """

    # membuat list
    matkul = ['Algoritma Dasar', 'Struktur Data', 'Perancangan Sistem']

    # menggunakan for untuk tipe data list
    for nRead in range(len(matkul)):
        print("%d: %s" % (nRead, matkul[nRead]))

if __name__ == "__main__":
    main()

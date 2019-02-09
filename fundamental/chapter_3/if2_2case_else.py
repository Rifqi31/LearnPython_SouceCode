#!usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : if2_2case_else.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk dua kasus
    """

    # membuat tuple
    namahari = ("minggu", "senin", "selasa",
                "rabu", "kamis", "jumat", "sabtu")

    # input untuk tipe data string
    hari = input("masukkan nama hari\t: ")

    # perintah if dengan dua ekspresi
    if hari.lower() == namahari[0] or \
            hari.lower() == namahari[6]:
        print(hari + " adalah hari libur")
    else:
        print("%s adalah hari kerja (bagi karyawan) " % hari)


if __name__ == "__main__":
    main()

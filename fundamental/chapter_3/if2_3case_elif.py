#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name : if2_3case_elif.py


def main():
    """
        Bab Statement Kontrol
        Bagian Struktur Pemilihan
        statement if untuk tiga kasus atau lebih
    """

    # input untuk nilai x dan y
    xnumber = int(input("masukkan nilai x\t: "))
    ynumber = int(input("masukkan nilai y\t: "))

    info = "Koordinat (" + str(xnumber) + "," + str(ynumber) + \
        ") berada pada Kuadran "

    # memeriksa nilai x dan y
    if xnumber > 0 and ynumber > 0:
        print(info + "I")
    elif xnumber < 0 and ynumber > 0:
        print(info + "II")
    elif xnumber < 0 and ynumber < 0:
        print(info + "III")
    elif xnumber > 0 and ynumber < 0:
        print(info + "IV")
    else:
        pass        # perintah kosong (tidak melakukan apapun)


if __name__ == "__main__":
    main()

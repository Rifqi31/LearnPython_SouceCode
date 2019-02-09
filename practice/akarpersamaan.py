# Python Version 3
# File Name : akarpersamaan.py
import math
import sys


def main():

    # menampilkan informasi program
    print("menampilkan & menghitung akar persamaan")

    # input from user
    a = int(input("masukkan nilai a\t: "))
    b = int(input("masukkan nilai b\t: "))
    c = int(input("masukkan nilai c\t: "))

    # melakukan proses perhitungan
    D = (math.pow(b, 2)) - (4 * a * c)

    if D < 0:
        print("angka berupa imajiner")
        sys.exit(1)
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = x1
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

    # menampilkan hasil
    print("\nx1 = %d" % x1)
    print("x2 = %d" % x2)

if __name__ == "__main__":
    main()

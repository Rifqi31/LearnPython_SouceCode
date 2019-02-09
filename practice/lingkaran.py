# Python Version 3
# File Name : lingkaran.py
import math

def main():
    # menampilkan informasi program
    print("luas dan keliling lingkaran")

    # input nilai jari-jari
    r = float(input("masukkan nilai jari-jari\t: "))

    # menghitung luas lingkaran
    l = math.pi * (r *  math.pow(2, 2))

    # menghitung keliling lingkaran
    k = 2 * math.pi * r

    # menampilkan hasil perhitungan ke layar
    print("Luas\t:", l)
    print("keliling\t:", k)


if __name__ == "__main__":
    main()

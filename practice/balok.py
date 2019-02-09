# Python Version 3
# File Name : balok.py

def main():
    # menampilkan informasi program
    print("Volume dan Luas Permukaan Balok\n")

    # input panjang, lebar, dan tinggi
    p = float(input("masukkan panjang\t: "))
    l = float(input("masukkan lebar\t: "))
    t = float(input("masukkan tinggi\t: "))

    # melakukan perhitungan
    V = p * l * t
    Lp = 2 * (p* l + p * t + l * t)

    # menampilkan hasil perhitunga ke layar
    print("\nVolume\t\t", V)
    print("Luas Permukaan\t: ", Lp)

if __name__ == "__main__":
    main()

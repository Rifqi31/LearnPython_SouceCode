# Python Version 3
# File Name : main_modul.py

import mymodule

def main():

    inputUser = float(input("masukkan jari - jari lingkarang\t: "))

    # memanggil fungsi yang ada pada module
    hasilluas = mymodule.luasLingkarang(inputUser)
    hasilkeliling = mymodule.kelilingLingkaran(inputUser)

    print("\nLuas Lingkaran\t: %d" % hasilluas)
    print("Keliling Lingkaran\t: %d" % hasilkeliling)

if __name__ == "__main__":
    main()

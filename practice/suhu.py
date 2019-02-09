# Python Version 3
# File Name : suhu.py

def main():
    # menampilkan informasi program
    print("Konversi suhu (Fahreinheit ke Celcius)\n")

    # input suhu dalam Fahreinheit
    F = float(input("masukkan suhu (Fahreinheit)\t: "))

    # melakukan konversi suhu ke Celcius
    C = 5 * (F - 32) / 2

    # menampilkan hasil konversi ke layar
    print("Fahreinheit\t: ", F)
    print("Celcius\t: ", C)


if __name__ == "__main__":
    main()

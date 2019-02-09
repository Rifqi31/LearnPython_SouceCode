# Python Version 3
# File Name : swap.py

def main():

    # menampilkan informasi program
    print("menukar nilai dari dua variabel\n")

    # input dari user
    varvalue1 = input("masukkan nilai variabel ke-1\t: ")
    varvalue2 = input("masukkan nilai variabel ke-2\t: ")

    # menampilkan nilai yang dimasukkan
    print("\nnilai sebelum ditukar")
    print("nilai variable ke-1\t: ", varvalue1)
    print("nilai variable ke-2\t: ", varvalue2)

    # melakukan pertukaran nilai
    varvalue3 = varvalue1
    varvalue1 = varvalue2
    varvalue2 = varvalue3

    # menampilkan nilai yang telah ditukar\
    print("\nnilai sesudah ditukar")
    print("nilai variable ke-1\t: ", varvalue1)
    print("nilai variable ke-2\t: ", varvalue2)


if __name__ == "__main__":
    main()

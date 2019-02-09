# Python Version 3
# File Name : maks3bilangan_2.py

def main():

    # menampilkan informasi program
    print("membandingkan tiga buah bilangan")

    # input dari user
    number1 = int(input("masukkan nilai ke-1\t: "))
    number2 = int(input("masukkna nilai ke-2\t: "))
    number3 = int(input("masukkan nilai ke-3\t: "))

    # melakukan operasi
    if number1 > number2 and number1 > number3:
        maks = number1
    else:
        if number2 > number1 and number2 > number3:
            maks = number2
        else:
            maks = number3
    
    # tampilkan output
    print("perbandingan dari %d, %d, %d adalah %d" % (number1, number2, number3, maks))


if __name__ == "__main__":
    main()

# Python Version 3
# File Name : maks2bilangan.py

def main():

    # menampilkan informasi program
    print("membandingkan dua buah bilangan")

    # input user
    number1 = int(input("masukkan nilai ke-1\t: "))
    number2 = int(input("masukkan nilai ke-2\t: "))

    # melakukan perbandingan
    if number1 > number2:
        maks = number1
    else:
        maks = number2

    
    # menampilkan hasil
    print("perbanding dari %d dan %d adalah %d" % (number1, number2, maks))


if __name__ == "__main__":
    main()

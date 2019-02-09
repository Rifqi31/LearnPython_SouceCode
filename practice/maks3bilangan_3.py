# Python Version 3
# File Name : maks3bilangan_3.py

def main():

    # menampilkan informasi program
    print("membandingkan tiga buah angka")

    # input from user
    number1 = int(input("masukkan nilai ke-1\t: "))
    number2 = int(input("masukkan nilai ke-2\t: "))
    number3 = int(input("masukkan nilai ke-3\t: "))

    # melakukan operasi
    maks = number1
    if number2 > maks : maks = number2
    if number3 > maks : maks = number3
    
    # menampilkan output
    print("perbandingan nilai dari %d, %d, %d adalah %d" % (number1, number2, number3, maks))

if __name__ == "__main__":
    main()

# Python Version 3
# File Name : maks6bilangan_4.py

def main():

    # menampilkan informasi program
    print("membandingkan enam buah bilangan")

    li_number = []

    for counter in range(1, 6+1):
        insert_value = int(input("masukkan nilai ke-%d\t: " % (counter)))
        li_number.append(insert_value)
    
    # menampilkan hasil input
    maks = max(li_number)
    print("nilai terbesar adalah %d" % (maks))


if __name__ == "__main__":
    main()

# Python Version 3
# File Name :  ratabilangan.py

def main():

    # menampilkan informasi program
    print("menghitung rata - rata bilangan")

    # list for contains numbers
    li_numbers = []

    # ask for user how much max range for list
    maxrange_li = int(input("masukkan nilai maksimal range dari list\t : "))

    total = 0

    for startCounter in range(0, maxrange_li):
        add_li = int(input("masukkan nilai ke-%d\t: " % (startCounter+1)))
        li_numbers.append(add_li)
        total += li_numbers[startCounter]
    
    # hitung rata - rata
    avarage = total / maxrange_li

    # tampilkan output
    print("\nrata - rata = %0.2f" % (avarage))

if __name__ == "__main__":
    main()

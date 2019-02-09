# Python Version 3
# File Name : detik_ke_jam.py

def main():

    # menampilkan informasi program
    print("\nkonversi detik ke jam\n")

    # input dari user
    totaldetik = int(input("masukkan detik \t: "))

    # melakukan konversi hh:mm:ss ke detik
    hh = totaldetik // 3600
    sisadetik = totaldetik % 3600
    mm = sisadetik // 60
    ss = sisadetik % 60

    # menampilkan hasil konversi
    print("%d detik sama dengan %d:%d:%d" % (totaldetik, hh, mm, ss))


if __name__ == "__main__":
    main()

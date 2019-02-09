# Python Version 3
# File Name : jam_ke_detik.py

def main():

    # menampilkan informasi program
    print("mengonversi jam ke detik")

    # input user
    hh = int(input("masukkan jumlah jam \t: "))
    mm = int(input("masukkan jumlah menit \t: "))
    ss = int(input("masukkan jumlah detik \t: "))

    # melakukan konversi hh:mm:ss ke detik
    totaldetik = (hh * 3600) + (mm * 60) + ss

    # menampilkan hasil konversi
    print("%d:%d:%d sama dengan %d detik" % (hh, mm, ss, totaldetik))

if __name__ == "__main__":
    main()

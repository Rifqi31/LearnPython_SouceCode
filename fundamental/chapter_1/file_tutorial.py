# Python Version 3
# File Name : file_tutorial.py

def main():

    # mengakses file
    datafile = open("sample.txt", "w")       # menampilkan objek file & metode "w" write

    # menulis ke dalam file
    datafile.write("Belajar pemrograman python dari 0\n")
    datafile.write("semoga saya bisa memahami materinya\n")
    datafile.close()

    # membaca file sample.txt
    for line in open("sample.txt"):
        print(line, end='')

if __name__ == "__main__":
    main()

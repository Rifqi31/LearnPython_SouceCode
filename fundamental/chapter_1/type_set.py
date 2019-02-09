# Python Version 3
# File Name : type_set.py

import sys

def printElements(s, info):
    print(info)
    if len(s) == 0:
        print("himpunan kosong \n")
        sys.exit(1)
    for e in s:
        print(str(e) + " ", end='')
    print("\n")

def main():
    # membuat himpunan
    s = set([11, 22, 23, 44, 55])
    printElements(s, "Elemen awal:")

    # menambahkan anggota/elemen baru
    # menggunakan metode add()
    s.add(66)
    s.add(77)
    printElements(s, "Setelah pemanggilan add() :")

    # menambah anggota/elemen baru
    # menggunakan metode update()
    s.update([88, 99])
    printElements(s, "Setelah pemanggilan update() :")

    # menghapus anggota dengan nilai 44
    s.remove(44)
    printElements(s, "Setelah pemanggilan remove() :")

    # menghapus semua anggota
    s.clear()
    printElements(s, "Setelah pemanggilan clear() :")

if __name__ == "__main__":
    main()

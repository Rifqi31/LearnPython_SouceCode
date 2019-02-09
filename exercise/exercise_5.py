# Python Version 3
# File Name : exercise_5.py

def main():
    # Exercise 5
    datalist1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    datalist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    dataresult = []

    for checkdata in datalist1:
        if checkdata in datalist2:
            if checkdata not in dataresult:
                dataresult.append(checkdata)
    

    print(dataresult)

if __name__ == "__main__":
    main()

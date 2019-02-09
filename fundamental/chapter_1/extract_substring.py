# Python Version 3
# File Name : extract_substring.py

def main():


    dataString = "Python"

    #   [-6]    [-5]    [-4]    [-3]    [-2]    [-1]
    #   P       y       t       h       o       n
    #   [0]     [1]     [2]     [3]     [4]     [5]

    print(dataString[0])        # P <--- ython
    print(dataString[1])        # P ---> y <--- thon
    print(dataString[-4])       # Py ---> t <--- hon
    print(dataString[:2])       # Py <--- thon
    print(dataString[2:])       # Py ---> thon
    print(dataString[1:4])      # P ---> yth <--- on
    print(dataString[2:5])      # Py ---> tho <--- n

if __name__ == "__main__":
    main()

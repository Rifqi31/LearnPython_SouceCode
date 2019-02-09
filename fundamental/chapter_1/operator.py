# Python Version 3
# File Name : operator.py


def main():

    # this value for operation
    numberValue1 = 22
    numberValue2 = 66
    liValue3 = [22, 44, 55, 88, 1, 3, 9, 10]

    # operator penugasan
    numberValue1 += 111
    # numberValue1 *= 2
    # numberValue1 //= 2 # pembagian bilangan bulat
    # numberValue1 /= 3.0 # pembagian bilangan rill
    # numberValue1 %= 3

    print(numberValue1)


    # operator aritmatika
    print(numberValue1 + numberValue2)
    print(numberValue2 - numberValue1)
    print(numberValue1 * 20)
    print(numberValue1 / 10)
    print(numberValue2 % 30)
    print(numberValue1 ** 2)
    print(numberValue2 // numberValue1)


    # operator relasional
    print(numberValue1 == numberValue2)
    print(numberValue1 <= numberValue2)
    print(numberValue1 >= numberValue2)
    print(numberValue1 < numberValue2)
    print(numberValue1 > numberValue2)
    print(numberValue1 != numberValue2)
    print(numberValue1 in liValue3)
    print(numberValue2 in liValue3)


    # operator logika
    print("\nlogical AND\n")
    print("True ^ False\t:", True and False)
    print("False ^ True\t:", False and True)
    print("True ^ True\t:", True and True)
    print("False ^ False\t:", False and False)

    print("\nlogical OR\n")
    print("True v False\t:", True or False)
    print("False v True\t:", False or True)
    print("True v True\t:", True or True)
    print("False v False\t:", False or False)

    print("\nlogical NOT\n")
    print("!True \t:", not True)
    print("!False \t:", not False)


    # operator string
    dataString1 = "back to basic for learning fundamental python"

    if "python" in dataString1 and "back" in dataString1:
        print("\noh yeah yeah!")
        print("practice make perfect")
    
    stringValue1 = "python"
    stringValue2 = "learning"

    print(stringValue1 + " " + "fundamental" + " " +stringValue2)
    print((stringValue1 + " ") * 5)


if __name__ == "__main__":
    main()
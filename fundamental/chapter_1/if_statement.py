# Pyhon Version 3
# File Name : if_statement.py


def main():

    value1 = float(input("insert value first\t: "))
    value2 = float(input("insert value second\t: "))

    op_input = input("insert operator (+, -, *, /, %)\t:")

    if op_input == "+":
        print("%.2f + %.2f = %.2f" % (value1, value2, value1+value2))
    elif op_input == "-":
        print("%.2f - %2f = %.2f" % (value1, value2, value1-value2))
    elif op_input == "*":
        print("%.2f * %.2f = %.2f" % (value1, value2, value1*value2))
    elif op_input == "/":
        print("%.2f / %.2f = %.2f" % (value1, value2, value1/value2))
    elif op_input == "%":
        print("%.2f modulus %.2f = %.2f" % (value1, value2, value1%value2))
    else:
        print("ERROR : please insert using this operator (+, -, *, /, %)")


if __name__ == "__main__":
    main()

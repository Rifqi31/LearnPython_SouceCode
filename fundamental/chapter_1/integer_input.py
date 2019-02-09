# Python Version 3
# File Name : integer_input.py

def main():
    # ask the user
    # variable = int(input(string))
    velocity = int(input("insert the velocity : "))
    mass = int(input("insert the time persecond : "))

    # set result
    total = velocity + mass

    # show the result
    print("result for mass is %d" % (total))

if __name__ == "__main__":
    main()

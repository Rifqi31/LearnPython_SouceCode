# Python Version 3
# File Name : float_input.py

def main():
    # ask the user
    velocity = float(input("insert vaulue for velocity : "))
    second = float(input("insert value for time per second : "))

    # set the result
    accelerate = velocity / second

    # show the result
    print("the value for accelerate is", accelerate)

if __name__ == "__main__":
    main()

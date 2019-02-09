# Python Version 3
# File Name : type_boolean.py

def main():
    # create logical table AND OR
    valueTrue = True
    valueFalse = False

    print("logical AND")
    # AND logical
    print("True ^ False")
    if valueTrue and valueFalse:
        print("true")
    else:
        print("false")
    
    print("\nlogical OR")
    # OR logical
    print("True v False")
    if valueTrue or valueFalse:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()

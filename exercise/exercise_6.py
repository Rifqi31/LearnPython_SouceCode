# Python Version 3
# File Name : exercise_6.py

def reverse(word):
    x = ' '
    for i in range(len(word)):
        x += word[len(word)-1 - i]
        return x

def main():

    inputUser = input("please enter the word\t: ")
    
    x = reverse(inputUser)

    if x == inputUser:
        print("This is palindrome")
    else:
        print("This is not palindrom")

if __name__ == "__main__":
    main()

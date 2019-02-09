# Python version 3
# File name : exercise_4.py

# create divisor
NumInput = int(input("insert your number :"))

listRange = list(range(1, NumInput+1))

divisorList = []

for number in listRange:
        if NumInput % number == 0:
                divisorList.append(number)

print(divisorList)

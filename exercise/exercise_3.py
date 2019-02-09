# Python version 3
# File name : exercise_3.py

# make list less than ten
listNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

insertNumber = int(input("insert number :"))

for i in listNumber:
        if i < insertNumber:
                new_list.append(i)


print(new_list)

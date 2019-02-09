# Python Version 3
# File Name : type_list.py

def main():

    # create simple list string
    grocery_list = ['Salad', 'Pizza', 'Coffe', 'Hotdog']

    # create simple list number
    grocery_price = [100, 500, 20, 30]

    # create list with string and numbers
    dataVideo = ['Make it happen baby', 120, 'Cum happy ending', 60, 'Ass is ass', 100]

    # show the result
    print(grocery_list[0], grocery_price[0])
    print(grocery_list[1], grocery_price[1])
    print(grocery_list[2], grocery_price[2])
    print(grocery_list[3], grocery_price[3])

    print(dataVideo[0], dataVideo[1])
    print(dataVideo[2], dataVideo[3])
    print(dataVideo[4], dataVideo[5])

    # add to the last index in the list
    grocery_list.append('Pecel Lele')

    # show the result
    print(grocery_list)

    # add to spesifix index in the list
    grocery_list.insert(0, 'Coccaine')

    # show the result
    print("\n", grocery_list)

    # add list to the specifix list
    grocery_list.extend(['Sushi', 'California Roll'])

    # show the result
    print("\n", grocery_list)

    # modify the value by index
    grocery_list[0] = 'Smoke ribs'

    # show the result
    print("\n", grocery_list)

    # delete some value
    grocery_list.remove('Smoke ribs')

    # show the result
    print("\n", grocery_list)

    # search some value, show index number
    print(grocery_list.index('Pecel Lele'))

if __name__ == "__main__":
    main()

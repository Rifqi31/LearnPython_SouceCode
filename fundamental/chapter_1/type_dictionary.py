# Python Version 3
# File Name : type_dictionary.py

def main():
    # creating a dictionary
    # variable = {key:value}
    # example make a 'Dictionary about english to indonesia'
    oxford_indo = {'Bird':"Burung", 'Jeraph':"Jerapah", 'Car':"Mobil", 'Pornstar':"Bintang Porno"}

    # numeric value dictionary
    numberStore = {'ValueNumber1': 20, 'ValueNumber2': 230, 'ValueNumber3': 444, 'ValueNumber4': 999}

    # string and numeric value dictionary
    multidataStore = {'TypeRace': "Elf", 'Job': "Acrobat", 'Strength': 100, 'Agility': 300, 'Intelegent': 120}

    # show value from dictionary
    print("Bird \t\t:", oxford_indo['Bird'])
    print("Jeraph \t\t:", oxford_indo['Jeraph'])
    print("Car \t\t:", oxford_indo['Car'])
    print("Pornstar \t:", oxford_indo['Pornstar'])

    total_sum = numberStore['ValueNumber1'] + numberStore['ValueNumber2'] \
                    + numberStore['ValueNumber3'] + numberStore['ValueNumber3']

    print(total_sum)

    print("\nRace \t\t\t:", multidataStore['TypeRace'])
    print("Job \t\t\t:", multidataStore['Job'])
    print("Strength \t\t:", multidataStore['Strength'])
    print("Agility \t\t:", multidataStore['Agility'])
    print("Intelegent \t\t:", multidataStore['Intelegent'], "\n")

    # adding value to dictionary
    oxford_indo['Table'] = "Meja"
    oxford_indo['Chair'] = "Kursi"

    # after add some keys and values
    print(oxford_indo)
    print("\n")

    # change value from dictionary
    numberStore['ValueNumber1'] = 100

    # after change value
    print(numberStore)
    print("\n")

    # delete some element from dictionary
    del numberStore['ValueNumber2']

    # show the result
    print(numberStore)



if __name__ == "__main__":
    main()

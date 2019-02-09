# Python Version 3
# File Name : type_set2.py

def main():

    this_set1 = set([22, 44, 2, 56])
    this_set2 = set([12, 21, 33, 43, 22, 12, 54])

    # union
    resultUnion = this_set1 | this_set2
    print(resultUnion)

    # intersection
    resultIntersection = this_set1 & this_set2
    print(resultIntersection)

    # difference
    resultDifference = this_set1 - this_set2
    print(resultDifference)

    # Symetric Difference
    resultSymetric = this_set1 ^ this_set2
    print(resultSymetric)

if __name__ == "__main__":
    main()

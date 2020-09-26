"""
Author: Rahul Ambati
Description: To convert an input string of Roman numerals to an Arabic integer
"""

RomanConversionDict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def get_input():
    userinput = input("TYPE ROMAN NUMERALS")
    try:
        arabiclist = [RomanConversionDict[value] for value in userinput]
    except KeyError:
        arabiclist = []
        print("ERROR: Invalid input found in string!")
        exit()

    return arabiclist


def get_sum(arabiclist):
    value = 0
    for i in range(len(arabiclist) - 1):
        if arabiclist[i] < arabiclist[i + 1]:
            value -= arabiclist[i]
        else:
            value += arabiclist[i]
    value += arabiclist[-1]

    return value


if __name__ == '__main__':
    result = get_sum(get_input())
    print("Arabic int is %d" % result)


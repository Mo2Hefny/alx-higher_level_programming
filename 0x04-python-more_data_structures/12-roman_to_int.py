#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(0, len(roman_string) - 1):
        if (romans[roman_string[i]] < romans[roman_string[i+1]]):
            num -= romans[roman_string[i]]
        else:
            num += romans[roman_string[i]]
    num += romans[roman_string[len(roman_string) - 1]]
    return num

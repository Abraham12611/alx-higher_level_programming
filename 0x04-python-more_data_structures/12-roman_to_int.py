#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 100, "D": 500}
    new_list = []
    for i in range(len(roman_string)):
        new_list.append(roman_dict[roman_string[i]])

    result = 0
    for i in range(len(new_list)):
        if new_list[i] > new_list[i -1]:
            result += new_list[i] * 2 - new_list[i -1]
        else:
            result += new_list[i]
    print(result)            

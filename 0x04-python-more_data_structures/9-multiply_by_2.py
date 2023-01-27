#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list_keys = list(a_dictionary.keys())
    list_keys.sort()
    for i in list_keys:
        print("{}: {}".format(i, a_dictionary.get(i) ** 2))

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        print("None")

    for keys in a_dictionary.keys():
        print("{}: {}".format(sort(keys), a_dictionary.get(keys)))

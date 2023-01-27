#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = [sum(set(my_list))]
    return new_list


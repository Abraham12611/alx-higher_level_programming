#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = [i for i in set_1 if not i in set_2]
    new_set1 = [i for i in set_2 if not i in set_1]
    return new_set + new_set1

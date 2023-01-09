#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    if number >= 0:
        last = number[-1]
    else:
        last = (number[-1]) * -1
        number = int(number)
    print(last, end="")
    return last

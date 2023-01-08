#!/usr/bin/python3
def uppercase(str):
	for i in range(len(str)):
  		if ord('a') <= ord(str[i]) <= ord('z'):
  		    letter = 32
  		else:
  	            letter = 0
  		print('{:c}'.format(ord(str[i]) - letter), end="")
print()

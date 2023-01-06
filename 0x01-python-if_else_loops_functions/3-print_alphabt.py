#!/usr/bin/python3
for i in range (97, 123):
	char = chr(i)
	if char != 'e' and char != 'q':
		print('{}'.format(chr(i)), end="")

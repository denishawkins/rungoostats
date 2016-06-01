#!/usr/bin/env python
# Module import sys
import sys

def celsius_to_fahr(temp_c):
	temp_f=temp_c* (9.0/5.0) +32
	return temp_f

def main()
	try:
		cels=float(sys.argv[1])
		print(celsious_to_fahr(cels))

	except:
		print("First argument must ne a number! if _name_ ="_main_")

print('hello')
print('These are the arguments: ',sys.argv)
print('This is the first arguments: ',sys.argv[0])
print('This is the first arguments: ',sys.argv[1])



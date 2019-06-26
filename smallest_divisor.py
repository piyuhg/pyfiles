#!/bin/usr/python3
num = int(input("Enter the number: "))
for i in range (2,num+1):
	if (num%i==0 ):
		print("Smallest divisor of {} is {}".format(num, i))
		break

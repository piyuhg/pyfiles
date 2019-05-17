#!/usr/bin/python3
num = int(input("Enter the number: "))
k = 0
for i in range(2,num):
	if(num%i==0):
		print("The entered number is a Composite Number")
		k = 1
		break
if(k==0):
	print("The entered number is a Prime Number")
	

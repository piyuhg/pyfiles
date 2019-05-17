#!/bin/usr/python3
n = int(input("Enter the number: "))
for i in range (1,n+1):
	a = []
	for j in range (1,i+1):
		print(j,end = " ")
		if (j<i):
			print("+",end = " ")
		a.append(j)
	print("=",sum(a))


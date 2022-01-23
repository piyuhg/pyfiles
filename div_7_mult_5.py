#!/usr/bin/python3
a = int(input("Enter the stating of the range: "))
b = int(input("Enter the last value of range: "))
k = 0
for i in range(a,b+1):
	if (i%5==0 and i%7==0):
		print(i,end =" ")
		k = 1
if (k==0):
	print("No more number in range!!")
else:
	print()

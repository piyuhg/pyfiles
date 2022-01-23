#!/usr/bin/python3
n = int(input("Enter the number of elements to be in the list: "))
a = []
for i in range(0,n):
	b = int(input("Enter the number: "))
	a.append(b)
num = int(input("Enter the nmber whose occurence is need to be checked: "))
c = 0
for i in a:
	if(i==num):
		c += 1
print("The number {} occured {} times".format(num,c))

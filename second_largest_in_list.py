#!/usr/bin/python3
n = int(input("Enter the number of items: "))
a = []
for i in range(0,n):
	a.append(int(input("Enter number: ")))
b = set(a)
b = list(b)
print("The second largest element in list is:",b[-2])

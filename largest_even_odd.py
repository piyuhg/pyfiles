#!/usr/bin/python3
n = int(input("Enter the number of elements to be in list: "))
a = []
for i in range(0,n):
	b = int(input("Element :"))
	a.append(b)
even, odd = [],[] 
for j in a:
	if (j%2==0):
		even.append(j)
	else:
		odd.append(j)
print("Even largest in list is:",max(even))
print("Odd largest in list is:",max(odd))


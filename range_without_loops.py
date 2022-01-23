#!/usr/bin/python3
def printno(upper):
	if(upper>1):
		printno(upper-1)
	print(upper,end=" ")
n = int(input("Enter the number: "))
printno(n)
print()

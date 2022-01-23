#!/bin/usr/python3
n = int(input("Enter the number: "))
def factorial(num):
	fact = 1
	for i in range(1,num+1):
		fact *= i
	return fact
def ncr(i,j):
	out = factorial(i)//(factorial(i-j)*factorial(j))
	return out
for i in range(0,n+1):
	print(" "*(n-i),end="")
	for j in range(0,i+1):
		print(ncr(i,j),end =" ")
	print()

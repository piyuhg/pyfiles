#!/usr/bin/python3
import math
def sineseries(x,n):
	sine = 0
	for i in range(n):
		sign = (-1)**n
		y = x*(math.pi)/180
		sine += sign*(y**(2*i+1))/math.factorial(2*i+1)
	return sine
n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
print("The sine series value is:",sineseries(x,n))

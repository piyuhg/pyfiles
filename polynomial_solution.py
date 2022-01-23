#!/bin/usr/python3
import math as m
order = int(input("Enter the order of equation: "))
coeffs = []
for i in range(0,order+1):
	coeff = int(input("Enter the coefficient value: "))
	coeffs.append(coeff)
x = int(input("Enter the variable value: "))
ans = 0
j = order
for i in coeffs:
	ans += i*m.pow(x,j)
	j -= 1
print("The solution of equation is:",ans)

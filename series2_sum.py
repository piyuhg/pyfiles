#!/usr/bin/python3
import math
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sumn = 0
for i in range(1,n+1):
	sumn = sumn + math.pow(x,i)/i
print(sumn)	

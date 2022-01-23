#!/usr/bin/python3
import math
def cosineseries(x,n):
	cos = 1
	sign = -1
	for i in range(2,n,2):
		y = x*math.pi/180
		cos += (y**i)*sign/math.factorial(i)
		sign = -sign	
	return cos
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
print(cosineseries(x,n))

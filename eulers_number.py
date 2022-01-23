#/usr/bin/python3
import math
n = int(input("Enter the number: "))
e = 1
for i in range(1,n+1):
	e += i/math.factorial(i)
print(e)

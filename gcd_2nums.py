#!/usr/bin/python3
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))		
gcd = 1
for i in range(1,min(a,b)+1):
	if (a%i==0 and b%i==0):
		gcd = i	
print("The GCD of the numbers is:",gcd)

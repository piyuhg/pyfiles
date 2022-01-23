#!/usr/bin/python3
num = int(input("Enter the number: "))
divs = [] 
for i in range(1,num//2+1):
	if(num%i==0):
		divs.append(i)
divs.append(num)
print("The divisors of the number are:",divs)	


#!/usr/bin/python3
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum1, sum2 = 0, 0
for i in range(1,a):
	if(a%i==0):
		sum1 += i
for i in range(1,b):
	if(b%i==0):
		sum2 += i
if(sum1 == b and sum2 == a):
	print("Numbers are amicable")
else:
	print("Numbers are not amicable")

#!/usr/bin/python3
n = int(input("Enter a number : "))
sum1 = 0
for i in range(1,n):
	if(n%i==0):
		sum1 += i
if (sum1==n):
	print("The entered number is a perfect number ")
else:
	print("The entered number is not a perfecr number ")

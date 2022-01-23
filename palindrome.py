#!/usr/bin/python3
num = int(input("Enter the number : "))
mun = 0
i = num
while i>0 :
	mun = mun*10 + i%10
	i //= 10
if mun==num :
	print("Palindrome Number")
else :
	print("Not a Palindrome Number")
	

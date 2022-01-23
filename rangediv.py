#!/usr/bin/python3
a = int(input("Enter the starting number : "))
b = int(input("Enter the last number : "))
num = int(input("Enter the number for division :"))
i = a
while i<=b :
	if i%num==0 :
		print(i," ")
	i+=1


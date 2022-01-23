#!/usr/bin/python3
num = int(input("Enter the number : "))
i = num
mun = 0
while(i>0):
	mun = mun*10 + i%10
	i//=10
print("The reverse of ",num," is ",mun)

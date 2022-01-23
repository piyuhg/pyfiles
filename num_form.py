#!/usr/bin/python3
num = int(input("Enter the number: "))
c = 0
a = num%10
temp = num
while num:
	num = num//10
	c+=1
newnum = c*10 + a
print("New number is: ",newnum)

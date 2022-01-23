#!/usr/bin/python3
num = int(input("Enter the number : "))
count = 0
i = num
while i>0 :
	count += 1
	i //=10
print(count)

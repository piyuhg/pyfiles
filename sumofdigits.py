#!/usr/bin/python3
num = int(input("Enter the number: "))
digsum = 0
i = num
while i > 0 :
	rem = i%10
	digsum = digsum + rem
	i //= 10
print(digsum)

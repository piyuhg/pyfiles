#!/usr/bin/python3
n = int(input("Enter the number of elements to be in list:  "))
a = []
even , odd, neg  = 0, 0, 0
for i in range (0,n):
	b = int(input(""))
	a.append(b)
for j in a:	
	if (j < 0) :
		neg += j
	elif (j%2 == 0):
		even += j
	elif (j%2!=0):
		odd += j
print("Entered List was:",a)
print("Sum of negative numbers is:",neg)
print("Sum of positive even numbers is:",even)
print("Sum of positive odd numbers is:",odd)
 
 
 

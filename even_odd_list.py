#!/usr/bin/python3
x = [1,2,3,3,2,1,4,5,6,3,4]
even = []
odd = []
for i in x:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print(x)
print(even)
print(odd)

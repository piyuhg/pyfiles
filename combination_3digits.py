#!/usr/bin/python3
a = input("Enter digit: ")
b = input("Enter digit: ")
c = input("Enter digit: ")
ls = []
ls.append(a)
ls.append(b)
ls.append(c)
for i in range (0, 3):
	for j in range (0, 3):
		for k in range (0,3):
			if(i!=j and j!= k and k != i):
				print(ls[i],ls[j],ls[k],sep="")


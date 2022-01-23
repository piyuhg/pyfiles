#!/usr/bin/python3
x = [1,2,3,3,2,1,4,5,6,3,4]
y = [3,26,8,3,5,2,9,0,1,4]
x.extend(y)
print(x)
y=y+x
print(y)
x.sort()
print(x)


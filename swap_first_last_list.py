#!/usr/bin/python3
x = [1,2,3,3,2,1,4,5,6,3,4]
print(x)
x[0] = x[0] + x[len(x)-1]
x[len(x)-1] = x[0] - x[len(x)-1]
x[0] = x[0] - x[len(x)-1]
print(x)


#!/usr/bin/python3
import math as m
a = int(input("Enter the side A: "))
b = int(input("Enter the side B: "))
c = int(input("Enter the side C: "))
s = (a+b+c)/2
area = m.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is:",area)

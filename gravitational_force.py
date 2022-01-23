#!/bin/usr/python3
m1 = float(input("Enter the first mass: "))
m2 = float(input("Enter the second mass: "))
r = float(input("Enter the distance between them: "))
G = 6.673 * (10**-11)
f = G*m1*m2/r**2
print("The gravitational force between them is: ",round(f,3),"N")

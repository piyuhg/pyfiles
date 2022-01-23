#!/usr/bin/python3
tempin = input("Enter the temperature: ")
val,unit = tempin.split(" ")
val = float(val)
if (unit =='c' or unit =='C'):
	tempout = (val*9/5) + 32
	print("Tempratur in farenheit is : {} F".format(tempout))
elif (unit =='f' or unit == 'F'):
	tempout = (val-32)*5/9
	print("Tempratur in celcius is : {} C".format(tempout))
else:
	print("Enter valid unit of temperature")


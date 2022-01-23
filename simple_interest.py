#!/usr/bin/python3
prin = int(input("Enter the principal value: "))
rate = int(input("Enter the rate of interest : "))
time = int(input("Enter the time period (in years): "))
si = prin*rate*time/100
amount = prin + si 
print("The simple interest would be :{} with amount : {}".format(si,amount))

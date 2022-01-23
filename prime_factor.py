#!/usr/bin/python3
num = int(input("Enter the integer: "))
sieve = set(range(2,num+1))
prime_list = []
while sieve:
	prime = min(sieve)
	prime_list.append(prime)
	sieve -= set(range(prime,num+1,prime))
prime_factor = []
for i in prime_list:
	if (num%i==0):
		prime_factor.append(i)
print("The prime factor of {} are : {}".format(num,prime_factor))


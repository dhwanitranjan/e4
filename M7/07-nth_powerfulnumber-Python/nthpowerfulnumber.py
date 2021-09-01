# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def prime(y):
	if y < 2:
		return False
	if y == 2:
		return True 
	if y%2 == 0:
		return False
	for i in range(3, round(y**0.5)+1, 2):
		if y % i == 0:
			return False
	return True

def powerfulnumber(x):
	for i in range(2, x+1):
		if prime(i):
			if x%i == 0:
				if x%i**2!=0:
					return False
	return True

def nthpowerfulnumber(n):
	guess = 0
	found = 0
	while found <= n:
		guess += 1
		if powerfulnumber(guess):
			found += 1
	return guess

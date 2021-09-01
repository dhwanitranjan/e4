# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def is309Num(n):
	new = []
	for i in range(10):
		new.append(str(i))
	x = str(n**5)

	for i in new:
		if i not in x:
			return False
	return True

def nthwithproperty309(n):
	guess = 309
	found = 1
	if n == 0:
	 	return 309
	while found <= n:
		guess += 1
		if (is309Num(guess)):
			found += 1
	
	return guess

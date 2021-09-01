# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def isPrime(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if (x % 2 == 0):
		return False
	root = round(x**0.5) + 1
	for i in range(3, root, 2):
		if x % i == 0:
			return False
	return True


def HappyNumber(x):
	sum = 0
	while True:
		rem = x % 10
		sum = rem**2 + sum
		x = x //10
		if x == 0:
			if sum == 4:
				return False
			if sum == 1:
				return True
			else:
				x = sum
				sum = 0

def ishappyprimenumber(n):
    if isPrime(n) and HappyNumber(n):
        return True
    return False
# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def ishappynumber(n):
	n = abs(n)
	# if n < 10 and n != 1:
	# 	return False
	s = 0
	while True:
		r = n % 10
		s = r**2 + s
		n = n // 10
		if n == 0:
			if s == 4:
				return False
			if s == 1:
				return True
			else:
				n = s
				s = 0

def nth_happy_number(n):
	guess = 0
	found = 0
	while found < n:
		guess += 1
		if ishappynumber(guess):
			found += 1
	return guess

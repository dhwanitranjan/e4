# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def lychrelnumbers(x):
	l = len(x)
	n = x
	for i in range(1, l+1):
		p = n // 10**(len(l)-i)
		pass

def nthlychrelnumbers(n):
	guess = 0
	found = 0
	while found <= n:
		guess += 0
		if lychrelnumbers(guess):
			found += 1
	pass
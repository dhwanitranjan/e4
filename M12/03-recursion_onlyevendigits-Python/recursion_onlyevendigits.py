# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
	if l == []:
		return []
	res = []
	for i in range(len(l)):
		n = l[i]
		new_num = 0
		c = 0
		while n > 0:
			r = n % 10
			if r % 2 == 0:
				new_num = new_num + r*(10**c)
				c += 1
			n = n // 10
			
		res.append(new_num)
	return res
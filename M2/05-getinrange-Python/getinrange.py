# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	# your code goes here
	if (x < bound1 and x > bound2) or (x > bound1 and x < bound2):
		return x
		
	if x < bound1 and x < bound2:
		if bound1 < bound2:
			return bound1
		else:
			return bound2
	
	if x > bound1 and x > bound2:
		if bound1 > bound2:
			return bound1
		else:
			return bound2

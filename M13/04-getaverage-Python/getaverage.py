# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s):
	l = s.split(",")
	t = 0.0
	c = 0
	for i in range(len(l)):
		if l[i].isnumeric():
			t += int(l[i])
			c += 1
	if c == 0:
		return 0.0
	else:
		return t/c

# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

# Prerequisite for the following problem is the above problem.
# Write the function inverseLookAndSay(a) that does the inverse of the above problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
	if a == [tuple()]:
		return []
	res = []
	for i in range(len(a)):
		l = list(a[i])
		for j in range(l[0]):
			res.append(l[1])
	return res
# def inverselookandsay(a):
# 	res = []
# 	t = []
# 	if a == []:
# 		return []
# 	for i in range(0, len(a)-1):
# 		c = 1
# 		if a[i] != a[i+1]:
# 			t.append(c)
# 			t.append(i)
# 			e = tuple(t)
# 			res.append(e)
# 		c += 1

# 	return res


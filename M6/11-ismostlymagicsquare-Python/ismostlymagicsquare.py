# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	s = 0
	d1 = 0
	d2 = 0
	for x in range(len(a)):
		s += a[0][x]
	for i in range(len(a)):
		r = 0
		c = 0
		for j in range(len(a)):
			r += a[i][j]
		if r!= s:
			return False
		for j in range(len(a)):
			c += a[j][i]
		if c!= s:
			return False                   #[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
	for k in range(len(a)):
		d1 += a[k][k]
	if d1 != s:
		return False
	
	i = len(a)-1
	j = 0
	while True:
		d2 += a[i][j]
		if i == 0:
			break
		i = i-1
		j = j+1
	if d2 != s:
		return False
	
	return True
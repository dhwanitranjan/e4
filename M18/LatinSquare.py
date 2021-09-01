# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == lst[len(lst)-i][len(lst)-j]:
                return True
            else:
                return False
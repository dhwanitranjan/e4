# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

# def limitedPowerSet(n, k):
#     l = []
#     sl = []
#     c = 1
#     l.append(set())
#     for i in range(1, n+1):
#         if c == k:
#             return l
#         l.append(set(i))
#         c += 1

import itertools

def findsubsets(s, x):
    return list(itertools.combinations(s, x))

def limitedPowerSet(n, k):
    l = []
    res = []
    res.append(())

    for i in range(1 , n+1):
        l.append(i)
    s = set(l)

    for x in range(1, n+1):
        sub = findsubsets(s, x)
        res += sub
    
    return res[:k]

print(limitedPowerSet(5, 7))

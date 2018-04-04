import time

start = time.time()
# # # Q.24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# # Sol.24
import itertools
a = [0,1,2,3,4,5,6,7,8,9]
go = itertools.permutations(a)
print(go)
print(list(itertools.permutations(a))[999999]) # 1000000번째이므로 999999

# A.24
#2783915460
end = time.time() - start
print(end)
#0.6875078678131104

import time
import itertools

start = time.time()
#  Q.53
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
# nCr =
# n!
# r!(n−r)!
# ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
# # Sol.53
def fac(n):
    i=1
    for j in range(1,n+1):
        i *= j
    return i

def combi(n,r):
    return int(fac(n)/(fac(r)*fac(n-r)))

a = []
for n in range(1,101):

    for r in range(1,n+1):
        b = combi(n,r)
        if b >= 1000000:
            a.append(b)

print(len(a))



# A.53
# 4075
# 0.05103659629821777

end = time.time() - start
print(end)

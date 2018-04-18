import time
import math
start = time.time()
# # Q.32
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# Sol.32
# a * b = c
# (1자리수) * (4자리수) = (4자리수)
for a1 in range(2,10):
    for b1 in range(1000,10000):
        c1 = a1 * b1
        a2 = list(str(a1))
        b2 = list(str(b1))
        c2 = list(str(c1))
        if len(set(b2)) ==4 and len(c2) == 4:
            d2 = a2 + b2 + c2
            if len(set(d2)) == 9 and '0' not in d2:
                # print(d2)
                print(c2)

# (2자리수) * (3자리수) = (4자리수)
for e1 in range(10,100):
    for f1 in range(100,1000):
        g1 = e1 * f1
        e2 = list(str(e1))
        f2 = list(str(f1))
        g2 = list(str(g1))
        if len(set(e2)) == 2 and len(set(f2)) == 3 and len(set(g2)) == 4 and len(g2) == 4:
            h2 = e2 + f2 + g2
            if len(set(h2)) == 9 and '0' not in h2:
                print(h2)
                print(g2)
# A.32
print(6952+7852+5796+5346+4396+7254+7632)
end = time.time() - start
print(end)
#

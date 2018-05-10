import time
import itertools

start = time.time()
#  Q.57
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
#  Sol.57
def bonsu(a,b):
    return (a+b,b)


a=[]
for n in range(1,1002):
    if n == 1:
        a.append(1)
    if n == 2:
        a.append(2)
    if n > 2 :
        b = a[n-2]*2 + a[n-3]
        a.append(b)
# print(a)

k=0
for i in range(0,1000):
    c = str(a[i]+a[i+1])
    d = str(a[i+1])

    if len(c) > len(d):
        k += 1

print(k)


# A.57
end = time.time() - start
print(end)

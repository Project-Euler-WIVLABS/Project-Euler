import time
import math
start = time.time()
# # # Q.34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Sol.34
def fac(n):
    j = 1
    i = 1
    for i in range(1,n+1):
        j *= i
        i = i+1
    return j

for a in range(3,1000000):
    b = str(a)
    c=0
    for x in range(0,len(b)):
        y = fac(int(b[x:x+1]))
        c += y
    # c = fac(int(b[0:1]))+fac(int(b[1:2]))+fac(int(b[2:3]))+fac(int(b[3:4]))+fac(int(b[4:5])) +fac(int(b[5:6]))
    if c == a:
        print(a)
    else :
        continue

# A.34
end = time.time() - start
print(end)
#
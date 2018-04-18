import time
import math
start = time.time()
# # Q.39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
# Sol.39
# a+b+c<=1000
# a+b>c
# a^2+b^2=c^2
for p in range(4,1001):
    d=0
    for c in range(1,int(p/2+1)):
        for b in range(1,p-c):
            a = p - c - b
            if  c < a + b and \
                    p == a + b + c and \
                    pow(c,2) == pow(b,2) + pow(a,2) and \
                    a<c and b<c and a<=b:
                    d += 1
                    print(p,d)
# A.39
# p = 840 d=8



end = time.time() - start
print(end)
#
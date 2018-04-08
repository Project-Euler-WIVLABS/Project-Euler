import time
import math

start = time.time()
# Q.12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
# Sol.12
import math
def triangle_num(n):
    return int(n*(n+1)/2)

def find_divisor(n):
    divisor=[]
    limit=int(math.sqrt(n))
    for i in range(1,limit+1):
        if n%i==0:
            divisor.append(i)
            divisor.append(int(n/i))
    return divisor

tmp=time.time()
answer=1
while  True:
    if len(find_divisor(triangle_num(answer)))>=500:
        print(triangle_num(answer))

        break
    else:
        answer+=1

# A.12
#
end = time.time() - start
print(end)
#
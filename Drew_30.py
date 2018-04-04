import time

start = time.time()
# # # Q.30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# Sol.30
# 3자리
import math

e3=[]
for i in range(100,1000):
    a = str(i)
    d = 0

    for j in range(0,3):
        b = a[j:j+1]
        c = int(b)
        # print(math.pow(c,5))
        d += math.pow(c,5)
    if d == i:
        e3.append(d)
    else:
        continue

print(e3)
#4자리
import math

e4=[]
for i in range(1000,10000):
    a = str(i)
    d = 0

    for j in range(0,4):
        b = a[j:j+1]
        c = int(b)
        # print(math.pow(c,5))
        d += math.pow(c,5)
    if d == i:
        e4.append(d)
    else:
        continue

print(e4)

# 5자리
import math

e5=[]
for i in range(10000,100000):
    a = str(i)
    d = 0

    for j in range(0,5):
        b = a[j:j+1]
        c = int(b)
        # print(math.pow(c,5))
        d += math.pow(c,5)
    if d == i:
        e5.append(d)
    else:
        continue

print(e5)

# 6자리
import math

e6=[]
for i in range(100000,1000000):
    a = str(i)
    d = 0

    for j in range(0,6):
        b = a[j:j+1]
        c = int(b)
        # print(math.pow(c,5))
        d += math.pow(c,5)
    if d == i:
        e6.append(d)
    else:
        continue

print(e6)

print(sum(e3+e4+e5+e6))
# A.30
# 443839
#
end = time.time() - start
print(end)
#4.318126440048218


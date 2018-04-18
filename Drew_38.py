import time

start = time.time()
# # Q.38
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
# Sol.38
for a1 in range(10,10000):
    d1 =''
    lens = 0
    for b1 in range(1,10):
        c1 = a1 * b1
        d1 += str(c1)
        lens += len(str(c1))
        if lens == 9:
            a=[]
            for i in range(0,9):
                a.append(d1[i:i+1])
            k = set(a)
            if len(k)==9 and '0' not in k:
                print(a1,a)

# A.38
end = time.time() - start
print(end)
#
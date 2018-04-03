import time
import math

start = time.time()
# # Q.28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# Sol.28
# 1001=2*500+1  -> n=500번째구하면됨
sum = 0
for n in range(3,1002,2):
    a = math.pow(n,2) + math.pow(n,2)-(n-1) + math.pow(n,2)-2*(n-1) + math.pow(n,2) -3*(n-1)
    sum += a

print((sum)+1)
# A.28
#669171001.0
time.sleep(0.1)
end = time.time() - start
print(end)
#0.0250159740447998


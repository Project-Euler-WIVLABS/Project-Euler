import time

start = time.time()
# # Q.14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
# Sol.14
max = 0
for m in range(1,1000000+1,1):
    num = m
    count = 1
    while m>1:
        count+=1
        if m%2==0:
            m = m//2
        else:
            m = 3*m+1
    if max < count:
        max = count
        max2= num
    print(num, count)
print(">>",max2,max)
# A.14
#
end = time.time() - start
print(end)
#

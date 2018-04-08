import time
import math
start = time.time()
# # Q.25
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# Sol.25
def d(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count


def fibo_nth(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a


n = 1
while True:
    if d(fibo_nth(n)) >= 1000:
        print(n)
        break
    n += 1

# A.25
#4782
end = time.time() - start
print(end)
# #2.3806893825531006


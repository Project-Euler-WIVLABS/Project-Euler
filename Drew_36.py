import time

start = time.time()
# # Q.36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# Sol.36
a=0
for i in range(1,1000001):
    j = list(reversed(str(i)))
    if list(str(i)) == j:
        g = bin(i)
        h = g[2:]
        k = list(reversed(str(h)))
        if list(str(h)) == k:
            a += i
            print(a)
# A.36
end = time.time() - start
print(end)
#
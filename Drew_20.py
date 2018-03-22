import time

start = time.time()
# # Q.20
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# Sol.20
def fac(n):
    mul = 1
    i=1
    while i<=n:
        mul *= i
        i = i+1
    return mul

print(fac(100))

# fac(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# 158자리
a = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"
b = 0
for i in range(0,158):
    c = int(a[i:i+1])
    b = b + c
print(b)
# A.20
# 648

time.sleep(0.1)
end = time.time() - start
print(end)
# 0.00078120231628418
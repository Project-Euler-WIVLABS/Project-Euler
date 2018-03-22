import time

start = time.time()
# # Q.15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

# Sol.15
def fac(n):
    mul=1
    i=1
    while i<=n:
        mul *= i
        i = i +1
    return mul

def short_case(a,b):
    return fac(a+b)/(fac(a)*fac(b))

print(short_case(20,20))
# A.15
time.sleep(0.1)
#
end = time.time() - start
print(end)
#0.0009984016418457

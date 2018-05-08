import time

start = time.time()
# # Q.46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# # Sol.46
def prime(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

c=[]
for n in range(0,10000):
    for b in prime(10000):
        a = 2*pow(n,2) + b
        c.append(a)
# print(sorted(list(set(c))))

d=[]
for i in range(1,10000,2):
    d.append(i)
# print(d)

for j in d:
    if j not in c:
        print(j)


# # A.46
end = time.time() - start
print(end)
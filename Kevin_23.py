import math
a = []
for i in range(12,28124):
    sum = 0
    for j in range(1,int(math.sqrt(i))+1):
        if i % j == 0:
            sum += j + i/j
        if j == math.sqrt(i):
            sum -= j
    sum = sum - i
    if sum > i:
        a.append(i)

b = set(a)

def abc(n):
    for i in b:
        if n < i:
            return False
        if (n - i) in b:
            return True
        else:
            continue

t = []
k = set(t)
for i in range(1,28124):
    if not abc(i):
        k.add(i)
    else:
        continue

v = list(k)
sum1= 0
for i in v:
    sum1 += i

print(sum1)
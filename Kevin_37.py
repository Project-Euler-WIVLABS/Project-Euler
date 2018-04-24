def prime(n):
    primes = [2, 3]
    if n < 2:
        return []
    if n == 2:
        return [2]
    for x in range(6, n + 2, 6):
        p = x - 1
        for y in primes:
            if y * y > p:
                break
            if p % y == 0:
                p = -1
                break
        if p != -1:
            primes.append(p)
        p = x + 1
        if p > n:
            break
        for y in primes:
            if y * y > p:
                break
            if p % y == 0:
                p = -1
                break
        if p != -1:
            primes.append(p)

    return primes


b = prime(800000)
a = []

for i in b:
    flag = True
    for j in range(len(str(i)), 0, -1):
        if int(str(i)[0:j]) in b:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        a.append(i)

c = []
for i in a:
    flag = True
    for j in range(0, len(str(i))):
        if int(str(i)[j:len(str(i))]) in b:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        c.append(i)

print(sum(c)- 17)
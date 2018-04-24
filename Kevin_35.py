def prime(n): #소수구하는 알고리즘
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

b = prime(1000000)
c = []
for a in b: #문자열순환시키기
    flag = True
    for i in range(1,len(str(a))):
        if int(str(a)[i:len(str(a))] + str(a)[0:i]) in b:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        c.append(a)
print(len(c))

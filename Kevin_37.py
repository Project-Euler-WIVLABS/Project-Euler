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


b = prime(800000)
a = []

for i in b: #소수중에서 오른쪽으로 자르면서 만족하는지 보기
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
for i in a: #오른쪽으로 자른 놈들중에서 왼쪽으로 자르면서 만족하는지 보기
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
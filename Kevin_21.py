def abc(n):
    a = []
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            a.append(i)
    for i in a:
        sum +=i
    return sum

c = []
for i in range(1,10001):
    if i != abc(i):
        if  i == abc(abc(i)):
            if i in c:
                continue
            else:
                c.append(i)
d = 0
for i in c:
    d +=i
print(d)

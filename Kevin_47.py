def soin(x):
    t = []
    d = 2
    while d <= x:
        if x % d == 0:
            t.append(d)
            x = x / d
        else:
            d = d + 1
    return t

a = 100
k = []
while True:
    t = soin(a)
    if len(set(t)) == 4:
        k.append(a)
    if a - 3 in k and a-2 in k and a - 1 in k and a in k:
        print(a-3)
        break
    a+=1
 
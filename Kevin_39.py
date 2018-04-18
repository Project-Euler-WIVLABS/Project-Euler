p = 1
max = 1
while p <= 1000:
    t = 0
    flag = True
    for i in range(1,500):
        if flag == False:
            break
        for j in range(1,500):
            if p - i - j > 0:
                k = p - i - j
                if (i * i) + (j * j) == (k * k):
                    t += 1
                    if max < t:
                        max = t
                        a = p
            else:
                flag = False
                break
    p += 1
print(a,max)
 
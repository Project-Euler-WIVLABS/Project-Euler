def P9():
    for i in range(1,333):
        for j in range(333,500):
            k = 1000 - i - j
            if (i*i) + (j*j) == (k * k):
                if i + j + k == 1000:
                    print(i,j,k)
                    return (i*j*k)
print(P9())

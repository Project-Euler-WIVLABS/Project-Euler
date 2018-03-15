def P9():
    for i in range(1,1000):
        for j in range(1,1000):
            if i < j :
                for k in range(1,1000):
                    if j < k:
                        if (i*i) + (j*j) == (k * k):
                            if i + j + k == 1000:
                                print(i,j,k)
                                return i,j,k
                    else:
                        continue
            else:
                continue


print(P9())

# def P9():
#     for i in range(1,333):
#         for j in range(333,500):
#             k = 1000 - i - j
#             if (i*i) + (j*j) == (k * k):
#                 if i + j + k == 1000:
#                     print(i,j,k)
#                     return (i*j*k)

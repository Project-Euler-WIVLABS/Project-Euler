import time

start = time.time()

# Q.7
# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

# # 이 때 10,001번째의 소수를 구하세요.


# Sol.7

a=[]

for i in range(2, 1000000):
    flag = False
    if i == 2:
        a.append(i)
    if i % 2 == 0:
        continue
    else:
        for j in a:
            if i % j != 0:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            a.append(i)
            if len(a) == 10001:
                break

print(a[10000])

# A.7
# 104743
end = time.time() - start
print(end)
# 4.953183174133301

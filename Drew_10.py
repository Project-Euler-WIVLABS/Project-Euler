import time

start = time.time()
# Q.10
# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# Sol.10

a=[ ]

for i in range(2,2000000):
    flag = False
    if i == 2:
        a.append(i)
    else:
        for j in a:
            if i % j != 0:
                flag=True
            else :
                flag=False
                break
        if flag == True:
            if i>2000000:
                break
            else :
                a.append(i)

print(sum(a))



# A.10
# 142913828922
end = time.time() - start
print(end)
# 1069.2314476966858

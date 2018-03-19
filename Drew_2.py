import time
start = time.time()

# Q.2
# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

# Sol.2-1
a=[]
def pivo(n):
    if n == 1:
        return 1
    if n == 2 :
        return 1
    else:
        return pivo(n-2) + pivo(n-1)

sum = 0
for n in range(1,1000):
    if pivo(n) > 4000000:
        break
    else :
        a.append(pivo(n))


for i in a:
    if i % 2 == 0:
        sum += i

print(sum)

# Sol.2-2
# a=1
# b=2
# c=0
# sum=0
# while a <= 4000000:
#     if a%2 ==0:
#         sum += a
#     c=a+b
#     a=b
#     b=c
# print(sum)

# A.2
# 4613732
end = time.time()-start
print(end)
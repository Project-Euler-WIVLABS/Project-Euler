import time
start = time.time()

# Q.3
# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.


# Sol.3-1
num=600851475143
for x in range(2,num):
    if num % x == 0:
        if x == num:
            break
        num = num /x
print(num)

#
# # Sol.3-2
# a=600851475143
# i=2
# b=0
# while i<=a:
#     if a%i==0:
#         b=i
#         a/=i
#     else:
#         i+=1
# print(b)

# A.3
6857
end = time.time()-start
print(end)

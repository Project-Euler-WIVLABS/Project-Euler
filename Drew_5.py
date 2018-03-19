import time

start = time.time()
# Q.5
# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까? <1~20의 최소공배수>

# Sol.5

# a =1
# for j in range(1,21):
#     a *= j
#     print(a)
# 1*2*3*...*20=2432902008176640000

a=0
for i in range(1,2432902008176640000):
    if i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 15== 0 and i % 14== 0 and i % 13== 0 and i % 12== 0 and i % 11== 0 :
        print(i)
        break



# A.5
# 232792560
end = time.time() - start
print(end)
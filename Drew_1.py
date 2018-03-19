import time
start = time.time()
# Q.1
# 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?


# Sol.1
sum1 = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum1 = sum1 + i

print(sum1)



# # Sol.1-2
# sum2 = 0
# i=0
# while i<1000 :
#
#     if i % 3 == 0 or i % 5 == 0:
#         sum2 = sum2 + i
#     i=i+1
#
# print(sum2)
#
# # Sol. 1-3
# print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))

# A.1
# 233168
end = time.time()-start
print(end)
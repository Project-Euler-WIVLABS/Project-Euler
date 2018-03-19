sum = 0 #1~100까지 각 수의 제곱을 더해서 담아놓을 공간
sum2 = 0 #1~100까지 각 수의 합을 담아놓을 공간
for i in range(1,101):
    sum += i*i
for j in range(1,101):
    sum2 += j
print(sum2*sum2- sum) #1~100까지 합의 제곱 - 1~100까지 각 수의 제곱을 더한 수


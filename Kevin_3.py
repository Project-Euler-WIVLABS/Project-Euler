a = 600851475143
#boolean 타입 isPrime으로 True를 가지고 나오는 숫자만 소수
for i in range(2,a):
    isPrime = True
    if a % i == 0:
        if i % 2 == 0: #짝수는 소수가 될 수 없으므로 제외
            continue
        else: #홀수인 약수들을 1부터 그 보다 1이 작은 수까지 나누면서 나누어지면 isPrime이 False이므로 제외
            for j in range(2,i):
                if i % j == 0:
                    isPrime = False
            if isPrime == True:
                print(i)
    else:
        continue


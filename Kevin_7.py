a = [2] #소수들을 담아놓을 리스트 생성, 2는 처음부터 0번째칸에 넣어놓음
for i in range(3,1000000000000000):
    isPrime = False #소수인지 판별하기위한 플래그
    if i % 2 == 0: #2를 제외하고 짝수는 소수가 될 수 없으므로 계산에서 제외
        continue
    for j in range(2,i):
        if i % j != 0: #i값을 0부터 i의 하나 작은 수들로 나누어서 플래그가 False로 바뀌지않으면 a에 적재
            isPrime = True
        else:
            isPrime = False
            break
    if isPrime == True: #플래그가 true이면 a에 적재
        a.append(i)
        print(i)
    if len(a) == 10001: #소수들을 담아놓은 리스트의 길이가 10001이면 10000번째 숫자가 정답
        print("10001번째 소수는 =%d"%a[10000])
        break



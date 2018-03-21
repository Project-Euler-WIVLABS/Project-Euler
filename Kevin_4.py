def palindrome():
    maxValue = 1000  # 초기 최대값은 1000
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if i * j < 100000 :
                break
            if str(i*j)[0:3] == str(i*j)[:2:-1]:
                if maxValue < i*j:#3자리수 * 3자리수를 문자열로 바꾼뒤 앞뒤로 뒤집어서 자른뒤 같은지 비교
                    maxValue = i*j
    return maxValue#다음부터 생성되는 값을 그 전 maxValue와 비교

print(palindrome())


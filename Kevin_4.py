a = [] #최대값을 담기위한 리스트
maxValue = 1000 #초기 최대값은 1000
for i in range(100,1000):
    for j in range(100,1000):
        if i * j < 100000 :
            continue
        if str(i*j)[0:3] == str(i*j)[:2:-1]: #3자리수 * 3자리수를 문자열로 바꾼뒤 앞뒤로 뒤집어서 자른뒤 같은지 비교
            if maxValue < (i*j): #초기값보다 크면 maxValue값 교체
                maxValue = i*j   #다음부터 생성되는 값을 그 전 maxValue와 비교
print(maxValue) 


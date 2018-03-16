import time
start = time.time()
# ###################기존에 작성한 코드##########################
# ###############################################################
a = [2]
sum = 0
for i in range(3,2000001,2):
    flag = True
    if i % 2 == 0 :
        continue
    for j in a:
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i)
        a.append(i)

for i in a:
    sum += i
print(sum)

end = time.time() - start  # end에 코드가 구동된 시간 저장
print(end) #기다릴 수 없을만큼 오래걸림

################################################################
###########에라토스테네스의 체 사용한 코드######################

a = []
for i in range(2000000): #2백만개의 공간을 우선 만들어둔다.
    a.append(i)
a[1] = 0
for i in range(2,2000000):
    if a[i] == 0: #이미 0인 공간은 건너뛰고 다음칸이 0인지 1인지 검사한다.
        continue
    for j in range(2,2000000): #자기 자신 i는 건너뛰고 i의 배수들은 전부다 0으로만든다.
        if i * j >= 2000000:  #최종i가 2백만을 넘으면 break
            break
        else:
            a[i*j] = 0 #i의 배수들, 소수는 어떤수의 배수가 될 수 없으므로 i의 배수들은 전부다 0으로 만든다.
sum = 0
for i in range(2000000): #200만까지 a리스트를 검사해서 0이아닌 i 인덱스 값들을 다 더하면 정답.
    if a[i] != 0:
        sum += i
print(sum)

end = time.time() - start  # end에 코드가 구동된 시간 저장
print(end) #실행시간 2초




a = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#1000자리의 숫자를 문자로 형변환한다 왜냐하면 인덱싱하기 위해서
c = []
d = []
maxValue = 1000 #초기 최대값 1000
for i in range(len(a)): #문자열a의 길이는 1000이므로 1자리씩 잘라서 리스트 c에 넣는다.
    print(i)
    c.append(a[i:i+1])

for i in range(len(a)):
    if i == 978: #리스트 c의 인덱스는 0~999이기때문에 i가 1000이되는 c에 접근하면 안되므로 i를 978까지만 제한한다.
        break
    #리스트 c의 담긴 문자를 정수로 바꾸어서 13개씩 끊어서 곱해보는데 중간에 0이 있는경우는 결과가 0이 되므로 계산에서 제외
    if int(c[i])*int(c[i+1])*int(c[i+2])*int(c[i+3])*int(c[i+4])*int(c[i+5])*int(c[i+6])*int(c[i+7])*int(c[i+8])*int(c[i+9])*int(c[i+10])*int(c[i+11])*int(c[i+12]) == 0:
        continue
    else: #리스트 c의 담긴 문자를 정수로 바꾸어서 13개씩 끊어서 곱해보는데 max값을 정해서 i값이 증가하면서 곱해지는 값과 최대값을 비교해 maxValue값을 계속해서 갱신한다.
        if maxValue < int(c[i])*int(c[i+1])*int(c[i+2])*int(c[i+3])*int(c[i+4])*int(c[i+5])*int(c[i+6])*int(c[i+7])*int(c[i+8])*int(c[i+9])*int(c[i+10])*int(c[i+11])*int(c[i+12]):
            maxValue = int(c[i])*int(c[i+1])*int(c[i+2])*int(c[i+3])*int(c[i+4])*int(c[i+5])*int(c[i+6])*int(c[i+7])*int(c[i+8])*int(c[i+9])*int(c[i+10])*int(c[i+11])*int(c[i+12])

print(maxValue) 
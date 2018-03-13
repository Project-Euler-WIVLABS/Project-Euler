#-*-coding: utf-8 -*-
sum = 0
a = []

#재귀함수
def PI(i):
    if i == 0 or i == 1:
        return i
    else:
        return PI(i-1) + PI(i-2)

#재귀함수호출하면서 반환값이 4000000이 넘지않으면 list(a)에 담기
for i in range(2,1000):
    if PI(i) < 4000000:
        a.append(PI(i))
    else:
        break


#짝수선별
for i in a:
    if i % 2 == 0:
        sum +=i
print(sum)









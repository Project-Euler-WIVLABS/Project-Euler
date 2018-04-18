def fac(n):
    t = [1,2,6,24,120,720,5040,40320,362880]
    if n == 0:
        return 1
    else:
        return t[n-1]

a= []
for i in range(145,1000000):
    sum = 0
    for j in range(len(str(i))):
        sum += fac(int(str(i)[j:j+1]))
    if sum == i:
        a.append(i)
        print(i)
sum = 0
for i in a:
    sum += i
print(sum)

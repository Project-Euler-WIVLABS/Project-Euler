def summ(n):
    a = 0
    for i in range(len(str(n))):
        a += int(str(n)[i])
    return a

max = 0
for i in range(2,101):
    for j in range(2,101):
        sum = 0
        print(i,j)
        sum = summ(pow(i,j))
        if max < sum:
            max = sum
print(max)
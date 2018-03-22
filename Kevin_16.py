a = str(2**1000)
sum = 0
for i in range(len(a)):
    sum += int(a[i:i+1])
print(sum)

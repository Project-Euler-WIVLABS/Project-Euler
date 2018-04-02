a = []
for i in range(10000000):
    a.append(0)
a[1] = 1
a[2] = 1
def PI(i):
    if a[i] == 0:
        a[i] =  PI(i-1) + PI(i-2)
    return a[i]

for i in range(1,10000000000):
    if PI(i) > 10**999:
        print(i)
        break

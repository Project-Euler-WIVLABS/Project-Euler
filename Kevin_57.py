a = 3
b = 2
c = 0
for i in range(1000):
    a = (a + b) + b
    b = a - b
    if len(str(a)) > len(str(b)):
        c += 1
    print(a,"/",b)

print(c)
def fac(a):
    i = 1
    b = 1
    while i <= a:
        b  *= i
        i += 1
    return b

sum = 0
for i in range(len(str(fac(100)))):
    sum += int((str(fac(100)))[i:i+1])
print(sum)

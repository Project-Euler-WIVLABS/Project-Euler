a = []
for i in range(1,1000000):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == bin(i)[2:][::-1]:
            a.append(i)
            print(a)

sum = 0
for i in a:
    sum += i
print(sum)

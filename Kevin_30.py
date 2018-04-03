t = []
def abc(n):
    return pow(n,5)

for i in range(2,295246):
    sum = 0
    for j in range(len(str(i))):
        if abc(int(((str(i))[j:j+1]))) > i:
            break
        sum += abc(int(((str(i))[j:j+1])))
    if sum == i:
        t.append(i)
print(t)

sum1 = 0
for i in t:
    sum1 += i
print(sum1)
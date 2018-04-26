def hab(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i:i+1])
    return sum

def gob(n):
    mul = 1
    for i in range(len(str(n))):
        mul *= int(str(n)[i:i+1])
    return mul

a = []
for i in range(1,10):
    for j in range(1000,10000):
        if len(str(i * j)) == 4:
            if i + hab(j) + hab(i*j) == 45:
                if i * gob(j) * gob(i*j) == 362880:
                    a.append(i*j)


for i in range(10,100):
    for j in range(100,1000):
        if len(str(i * j)) == 4:
            if hab(i) + hab(j) + hab(i*j) == 45:
                if gob(i) * gob(j) * gob(i*j) == 362880:
                    a.append(i*j)

print(sum(list(set(a)))-9954)

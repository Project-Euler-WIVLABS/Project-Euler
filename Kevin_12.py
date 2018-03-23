import math
b = []
for i in range(50,100000000000):
    a = int(i*(i+1)/2)
    for j in range(1,int(math.sqrt(a)+1)):
        if a % j == 0:
            if isinstance(math.sqrt(a),int) == True:
                b.append(j)
                b.append(j)
                b.pop(0)
            else:
                b.append(j)
                b.append(j)
    if len(b)>=500:
        break
    else:
        b.clear()
print(a)

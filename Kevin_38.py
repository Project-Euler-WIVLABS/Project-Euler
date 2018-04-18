def mul(t):
    a = 1
    for i in t:
        a *= int(i)
    return a
def sum(t):
    a = 0
    for i in t:
        a += int(i)
    return a

def abc():
    max = 1
    for i in range(1,10000):
        t= ''
        for j in range(1,6):
            t += str(i*j)
            if len(t) == 9:
                if mul(t) == 362880:
                    if sum(t) == 45:
                        if max < int(t):
                            max = int(t)
            elif len(t) < 9:
                continue
            else:
                break
    return max
print(abc())
def pen(n):
    return str(n) == str(n)[::-1]
def reverse(n):
    return int(str(n)[::-1])

b = 0

for i in range(1,10001):
    flag = True
    for j in range(50):
        if pen(i + reverse(i)):
            flag = True
            break
        else:
            i = i + reverse(i)
            flag = False
    if flag == False:
        b += 1
print(b)
def abc(i,f):
    f+=1
    if i % 2 == 0:
        i = int(i / 2)
        if i == 1:
            return f
        else:
            return abc(i,f)
    else:
        i = 3*i + 1
        if i == 1:
            return f
        else:
            return abc(i,f)
maxlong = 1
for i in range(1000001,0,-1):
    if abc(i,0) > maxlong:
        maxlong = abc(i,0)
        print(maxlong+1,i)


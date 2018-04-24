a = []
for i in range(10,100): #분모
    for j in range(10,i): #분자
        if str(i)[1:2] != '0':
            if str(i)[0:1] == str(j)[1:2]:
                if int(str(j)[0:1]) / int(str(i)[1:2]) == j / i:
                    print(j,"/",i)

a = []
for i in range(2,101):
    for j in range(2,101):
        if pow(i,j) in a:
            continue
        else:
            a.append(pow(i,j))
print(len(a))
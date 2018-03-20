a = 600851475143
i = 2
while i<a:
    if a % i == 0:
        a /= i
    else:
        i+=1
print(i)



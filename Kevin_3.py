a = 600851475143
i = 3
while i<a:
    if a % i == 0:
        a /= i
    else:
        i+=2
print(i)
 


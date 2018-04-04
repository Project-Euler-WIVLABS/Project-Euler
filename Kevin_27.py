import math
def abc(i,j):
    for n in range(100):
        if ab((n * n) + (i * n) + j):
            print((n * n) + (i * n) + j)
            continue
        else:
            return n

def ab(k):
    isPrime = False
    if k > 0:
        for j in range(2, int(math.sqrt(k)) + 1):
            if k % j != 0:
                isPrime = True
            else:
                return False
        if isPrime == True:
            return True
    else:
        for j in range(-2,k,-1):
            if k % j != 0:
                isPrime = True
            else:
                return False
        if isPrime == True:
            return True

maxprime = 0
a = []
b = 0
c = 0
for i in range(-999,1000):
    for j in range(-999,1000):
        if abc(i,j) > maxprime:
            maxprime = abc(i,j)
            b = i
            c = j

print(b,c)  
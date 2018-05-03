import time
import itertools
from itertools import permutations

start = time.time()
#  Q.49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
# Sol.49
def prime(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

a = sorted(set(prime(10000)) - set(prime(999)))
# print(a)
for i in a:
    b = list(permutations(list(str(i))))
    e=[]
    for j in range(0,24):
        c= b[j]
        d= c[0]+c[1]+c[2]+c[3]
        e.append(d)
    f = sorted(set(e))

    # print(i,f)
    average=[]
    for h in f:
        result = (int(h) + i)/2
        if result != i:
            average.append(str(int(result)))
    # print(i,average,f)



    for x in average :
        if x in f:
            if i != int(x) :
                f1=int(x)
                f2=2*int(x)-i
                if f1 in a and f2 in a:
                    # print(i,f1,f2)
                    print(str(i)+str(f1)+str(f2))




# A.49
end = time.time() - start
print(end)
#296962999629

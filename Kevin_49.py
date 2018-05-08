import itertools
def prime(n):
   if n < 2:
       return []
   s = [0, 0] + [1] * (n - 1)
   for i in range(2, int(n**.5)+1):
       if s[i]:
           s[i*2::i] = [0] * ((n - i)//i)
   return [i for i, v in enumerate(s) if v]
a = prime(10000)

def abc(v):
    for x,a in enumerate(v[:-2]):
        for b in v[x+1:]:
            c = b * 2 - a
            if c in v:
                print(a , b , c)
                return


for i in a:
    v = []
    if i>1000:
        t = []
        t = list(map(int,set(map("".join, itertools.permutations(str(i))))))
        for j in t:
            if len(str(j)) == 4 and j in a:
                v.append(j)
        if len(v) > 3:
            v.sort()
            abc(v)
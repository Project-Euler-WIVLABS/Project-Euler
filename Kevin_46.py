import math
def prime(n):
   if n < 2:
       return []
   s = [0, 0] + [1] * (n - 1)
   for i in range(2, int(n**.5)+1):
       if s[i]:
           s[i*2::i] = [0] * ((n - i)//i)
   return [i for i, v in enumerate(s) if v]


i = 35
is_true = True

while is_true:
    j = True
    if i not in prime(i):
        for k in prime(i):
            if j == False:
                break
            for t in range(1,int(math.sqrt(i))+1):
                if i == k + 2 * pow(t,2):
                    j = False
                    break
        if j == True:
            print(i)
            is_true = False
    i += 2

import time
import itertools

start = time.time()
#  Q.56
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# Sol.56
c=[]
for a in range(2,100):
    for b in range(1,100): 
        d = pow(a,b)
        e = list(str(d))
        f=0
        for i in range(0,len(e)):
            f += int(e[i])
            # print(f)
            c.append(f)

print(max(c))

# A.56
end = time.time() - start
print(end)

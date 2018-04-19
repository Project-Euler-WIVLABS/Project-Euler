import time

start = time.time()
# # # Q.21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
# Sol.21
z={}
for i in range(10,10001):
    k = []
    for j in range(1,int(i/2+1)):

        if i%j!=0 :
            continue
        if i%j==0:
            k.append(j)

    g = sum(k)
    b=[]
    for a in range(1,int(g/2+1)):

        if g%a !=0:
            continue
        if g%a == 0 :
            b.append(a)
    c = sum(b)
    if c==i:
        print({i,g})

# A.21
#(220,284)/(1184,1210)/(2924,2620)/(5564,5020)/(6232,6368)
print(220+284+1184+1210+2924+2620+5564+5020+6232+6368)

end = time.time() - start
print(end)
#

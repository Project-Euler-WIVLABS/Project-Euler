import time
import itertools

start = time.time()
#  Q.52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# # Sol.52
#(6자리수)

for i in range(100000,int(1000000/6)+1):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    for i2 in range(0,6):
        a.append(str(i)[i2])
        b.append(str(2*i)[i2])
        c.append(str(3*i)[i2])
        d.append(str(4*i)[i2])
        e.append(str(5*i)[i2])
        f.append(str(6*i)[i2])
    a2 = sorted(a)
    b2 = sorted(b)
    c2 = sorted(c)
    d2 = sorted(d)
    e2 = sorted(e)
    f2 = sorted(f)
    if a2==b2==c2==d2==e2==f2:
        print(i)
#(7자리수)
# for j in range(1000000,int(10000000/6)+1):
#     a=[]
#     b=[]
#     c=[]
#     d=[]
#     e=[]
#     f=[]
#     for j2 in range(0,6):
#         a.append(str(j)[j2])
#         b.append(str(2*j)[j2])
#         c.append(str(3*j)[j2])
#         d.append(str(4*j)[j2])
#         e.append(str(5*j)[j2])
#         f.append(str(6*j)[j2])
#     if a==b==c==d==e==f:
#         print(j)

# A.52
# 142857
# 1.0117194652557373

end = time.time() - start
print(end)

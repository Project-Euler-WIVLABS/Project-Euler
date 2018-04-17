import time

start = time.time()
# # Q.40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# 1*9+2*90+3*900+4*9000+5*
# # Sol.40
a=[]
t = ''
for i in range(1,10000000):
    a.append(i)
    if i==999999:

        for j in a:
            t+=str(j)

        break

d1= print(t[0:1])
d10= print(t[9:10])
d100= print(t[99:100])
d1000= print(t[999:1000])
d10000= print(t[9999:10000])
d100000= print(t[99999:100000])
d1000000= print(t[999999:1000000])
 
c = int(t[0:1]) * int(t[9:10]) * int(t[99:100]) * int(t[999:1000]) * int(t[9999:10000]) * int(t[99999:100000]) * int(t[999999:1000000])
print(c)
    # print(t[8:9])
# # A.40
end = time.time() - start
print(end)
# #
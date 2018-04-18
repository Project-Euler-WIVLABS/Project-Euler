import time
import math
start = time.time()
# # # Q.33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# Sol.33
# i 분모 j  : 분자
#분모 앞자리, 분자 뒷자리 빼고 구하기
for i in range(10,100):
    for j in range(10,i-1):
        a = str(i)[1:2]
        a1 = str(i)[0:1]
        b = str(j)[0:1]
        b1 = str(j)[1:2]
        if int(a) != 0 :
            if int(a1)==int(b1) and j/i == int(b) / int(a):
                if j/i <1:
                    print(j,i)


#분모 뒷자리, 분자 앞자리 빼고 구하기
for k in range(10,100):
    for h in range(10,k):
        d = str(k)[0:1]
        d1 = str(k)[1:2]
        e = str(h)[1:2]
        e1 = str(h)[0:1]
        f = int(e) / int(d)
        if int(d1)==int(e1) and h/k == f:
            print(h,k)


# A.33
#(16,64) * (26,65) * (19,95) * (49,98)
#(1,4) * (2,5) * (1,5) * (1,2)

#(1,100)
end = time.time() - start
print(end)
#
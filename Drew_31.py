
import time
import itertools

start = time.time()
#  Q.31

# # Sol.31
b,c,d,e,f,g,h = 100,50,20,10,5,2,1

sum = 0
for i2 in range(0,3):
    for i3 in range(0,5):
        if b*i2 + c*i3 > 200:
            break
        for i4 in range(0,11):
            if b * i2 + c * i3  + d * i4> 200:
                break
            for i5 in range(0,21):
                if b * i2 + c * i3 + d * i4 + e * i5 > 200:
                    break
                for i6 in range(0,41):
                    if b * i2 + c * i3 + d * i4 + e * i5 + f*i6 > 200:
                        break
                    for i7 in range(0,101):
                        if b * i2 + c * i3 + d * i4 + e * i5 + f * i6 + g * i7> 200:
                            break
                        for i8 in range(0,201):
                            if b * i2 + c * i3 + d * i4 + e * i5 + f * i6 + g * i7 + h * i8 > 200:
                                break
                            elif b * i2 + c * i3 + d * i4 + e * i5 + f * i6 + g * i7 + h * i8 == 200:
                                sum += 1
                                # print(i2,i3,i4,i5,i6,i7,i8)
print(sum+1)
# +1 의 의미 200펜스*1 일때 경우의 수 하나
# A.31
end = time.time() - start
print(end)

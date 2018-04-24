import time
import math
start = time.time()
#  Q.48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
# Sol.48
sum = 0
for a in range(1,1001):
    sum += pow(a,a)

print(str(sum)[-10:])
# A.48
end = time.time() - start
print(end)
#9110846700
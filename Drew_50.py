import time

start = time.time()
#  Q.50
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# Sol.50
def prime(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

a = prime(1000000)
print(a)

sum = 0
for i in range(0,len(a)):
    sum += a[i]
    if sum <= 1000000:
        print(sum)
        if sum in a:
            print(sum)

# A.50
# 997651
end = time.time() - start
print(end)
#0.5603981018066406

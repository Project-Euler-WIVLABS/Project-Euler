def mul(n):
    return pow(n,2)


def is_prime(n):
  if n < 2:
      return False
  if n in (2, 3):
      return True
  if n % 2 is 0 or n % 3 is 0:
      return False
  if n < 10:
      return True
  k, l = 5, n ** 0.5
  while k <= l:
    if n % k == 0 or n % (k + 2) == 0:
        return False
    k += 6
  return True

i = 3
num = 1
prime = 0
while True:
    a = mul(i)-2*num
    if is_prime(a):
        prime += 1
    b = mul(i)-4*num
    if is_prime(b):
        prime += 1
    c = mul(i)-6*num
    if is_prime(c):
        prime += 1
    print(float(prime)/(i*2 - 1))
    if float(prime) / (i*2 - 1) < 0.1:
        print(i)
        break
    num += 1
    i += 2

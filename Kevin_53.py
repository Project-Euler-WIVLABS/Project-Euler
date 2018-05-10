def fac(n):
  fac = 1
  for i in range(1, n + 1):
    fac *= i
  return fac


def abc(n):
    k = 0
    for r in range(1,n+1):
        if fac(n) / (fac(r)*fac(n-r)) >= 1000000:
            k += 1
    return k

k = 0
for n in range(23,101):
    k+=abc(n)
print(k)

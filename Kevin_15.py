def fac(n):
    i = 1
    a = 1
    while i<=n:
        a *= i
        i += 1
    return a

print(fac(40) / (fac(20) * fac(20)))

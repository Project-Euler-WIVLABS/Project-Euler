def Pn(n):
    return (n * (3*n - 1))/2

def is_hexagonal(k):
    n = (((8*k+1) ** 0.5) + 1 ) /4
    return int(n) == n

def abc():
    n = 166
    is_true = True
    while is_true:
        if is_hexagonal(Pn(n)):
            print(Pn(n))
            is_true = False
        n += 1
abc()

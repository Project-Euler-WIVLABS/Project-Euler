# Q.10
# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# Sol.10
a=[]
def prime(n):
    if n ==2:
        print n
    for i in range(2,n):
        if n % i == 0:
            break
        elif i == n - 1:
            print n

# A.10
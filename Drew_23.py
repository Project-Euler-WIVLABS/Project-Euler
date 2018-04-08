import time

start = time.time()
# # Q.23

# Sol.23
from math import sqrt

# 진약수 구하기
def factorization(number):
    factors = []
    for n in range(1, int(sqrt(number))+1):
        if number % n == 0:
            if n not in factors:
                factors.append(n)
            if (number//n) not in factors:
                factors.append(number // n)
    factors.sort()
    factors.remove(number)
    return factors

# 초과수인지 판별하기
def is_abundant(number):
    proper_divisors = factorization(number)
    return number < sum(proper_divisors)
 
# 초과수들
abundant_numbers = set([number for number in range(12, 28123) if is_abundant(
        number)])

# 초과수들의 합
sum_abundant_numbers = set([x+y for x in abundant_numbers for y in
                       abundant_numbers])

# 일반 숫자에서 초과수들의 합을 뺀다.(집합 연산)
numbers = set([number for number in range(1, 28123)]) - sum_abundant_numbers

# 초과수들의 합으로 표현할 수 없는 숫자들의 합
print(sum(list(numbers)))
# A.23
#
end = time.time() - start
print(end)
#
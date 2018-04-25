def prime(n):
   if n < 2:
       return []
   s = [0, 0] + [1] * (n - 1)
   for i in range(2, int(n**.5)+1):
       if s[i]:
           s[i*2::i] = [0] * ((n - i)//i)
   return [i for i, v in enumerate(s) if v]

a = prime(10000000)
max = 0
for i in a:
    sum = 0
    mul = 1
    for j in range(len(str(i))):
        mul *= int(str(i)[j:j+1])
        if mul == 0:
            break
        sum += int(str(i)[j:j+1])
        if sum > 28:
            break
        if mul > 5040:
            break
    if sum == 28 and mul == 5040 and len(str(i)) == 7:
        if max < i:
            max = i
    elif sum == 21 and mul == 720 and len(str(i)) == 6:
        if max < i:
            max = i
    elif sum == 15 and mul == 120 and len(str(i)) == 5:
        if max < i:
            max = i
    elif sum == 10 and mul == 24 and len(str(i)) == 4:
        if max < i:
            max = i
print(max)
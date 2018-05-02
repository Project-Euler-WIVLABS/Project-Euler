with open('words.txt','r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()


def T(n):
    a = []
    for i in range(1,n+1):
        a.append(int((i * (i+1))/2))
    return a

c = []
for i in range(len(words)):
    b = 0
    for j in words[i]:
        b += (ord(j)-64)
    if b in T(50):
        c.append(words[i])

print(len(c))

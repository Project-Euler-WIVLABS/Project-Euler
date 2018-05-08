import itertools

for i in range(10,17):
    t = list(map(int, set(map("".join, itertools.permutations(str(i))))))
    if i * 2 in t and i * 3 in t and i * 4 in t and i * 5 in t and i * 6 in t:
        print(i)
        break

for i in range(100,167):
    t = list(map(int, set(map("".join, itertools.permutations(str(i))))))
    if i * 2 in t and i * 3 in t and i * 4 in t and i * 5 in t and i * 6 in t:
        print(i)
        break

for i in range(1000,1667):
    t = list(map(int, set(map("".join, itertools.permutations(str(i))))))
    if i * 2 in t and i * 3 in t and i * 4 in t and i * 5 in t and i * 6 in t:
        print(i)
        break

for i in range(10000,16667):
    t = list(map(int, set(map("".join, itertools.permutations(str(i))))))
    if i * 2 in t and i * 3 in t and i * 4 in t and i * 5 in t and i * 6 in t:
        print(i)
        break

for i in range(100000,166667):
    t = list(map(int, set(map("".join, itertools.permutations(str(i))))))
    if i * 2 in t and i * 3 in t and i * 4 in t and i * 5 in t and i * 6 in t:
        print(i)
        break

import math
def is_pn(n):
    n = abs(n)
    p = (math.sqrt(24*n + 1) + 1) / 6

    return p == int(p)

i = 0
pent_list = [1]
not_found = True

while not_found:
    i += 1
    pent_list.append(int(i*(3*i - 1)/2))
    for j in range(len(pent_list)):
        if is_pn(pent_list[i] - pent_list[j]) and is_pn(pent_list[i]+pent_list[j]):
            print(pent_list[i] - pent_list[j])
            not_found = False
            break

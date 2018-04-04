sum = 1
for i in range(3,1002,2):
    sum += pow(i,2) + (pow(i,2) - ((i-1)*1)) + (pow(i,2) -(i-1)*2) + (pow(i,2) -(i-1)*3)
print(sum)
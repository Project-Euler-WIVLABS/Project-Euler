count_sunday = 0
total_day = 0
end_day = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1900,2001):
    for j in range(12):
        if i % 4 == 0 and i % 100 != 0 and j == 1:
            total_day += end_day[j]+1
        else:
            total_day += end_day[j]

        if (total_day - 6) % 7 == 0 and i > 1900:
            count_sunday += 1
            print(i,j+1,"**")
print(count_sunday - 1)




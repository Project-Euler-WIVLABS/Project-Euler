import time

start = time.time()
# # Q.19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday. - 1900.01.01(월)
# Thirty days has September, April, June and November. 4,6,9,11 - 30일
# All the rest have thirty-one, 1,5,7,8,10,12 - 31일
# Saving February alone, Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 2월 - 29일(4로나눠지는날)/28일(그외, 400으로 나눠지지 않은수중에 100번째마다-404,808,1212,1616,2020[해당x[)

# Sol.19
from calendar import weekday
c = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if weekday(y, m, 1)==6:
            c += 1
print(c)
# A.19
#
end = time.time() - start
print(end)
#
171



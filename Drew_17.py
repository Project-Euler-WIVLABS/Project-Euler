import time

start = time.time()
# Q.17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# 1~99
# "one~nine"*9
# "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety"*10
# "ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen"

enwkfltn = (3+3+5+4+3+3+5+5+4+3)*9 + (6+6+5+5+5+7+6+6)*10 + (3+6+6+8+8+7+7+9+8+8)

# 100~999
# (one+two+...+nine)*100 hundred*900
# and*99*9
# +1~99 * 9

tpwkfltn = enwkfltn*9 + ((3+3+5+4+3+3+5+5+4+3)*9*10 + 7*9*100 + 3*9*99)

# 1000
one_thousand = 11

sum = enwkfltn + tpwkfltn + one_thousand

print(enwkfltn)
print(tpwkfltn)
print(sum)


# Sol.17
21124
# A.17
#
time.sleep(0.1)
end = time.time() - start
print(end)
#0.00067129135131836

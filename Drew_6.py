import time
start = time.time()

# Q.6
# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).

# 12 + 22 + ... + 102 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.

# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?

# Sol.6
wprhqdmlgkq = 0
gkq = 0
for i in range(1,101):
    wprhqdmlgkq += i*i
for j in range(1,101):
    gkq += j
gkqdmlwprhq = gkq ** 2
    
print(gkqdmlwprhq-wprhqdmlgkq)
# A.6
#25164150

end = time.time()-start
print(end)
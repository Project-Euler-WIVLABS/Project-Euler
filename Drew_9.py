import time
start = time.time()

# Q.9
# 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
# 예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2이므로 3, 4, 5는 피타고라스 수입니다.
# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

# 조건 : a+b > c -> a+b+c > 2c -> c < 500 -> c^2<500^2 -> a^2+b^2<500^2 -> 2*a^2<500^2 -> a<250*root(2) =simliar 357


            
# Sol.9

for a in range(0,357):
    
    for b in range(a,500):
        
        ab = a + b
        
        if (a*a)+(b*b) == (1000-ab)*(1000-ab):
           
            print(a*b*(1000-ab))            

# A.9
# 31875000
end = time.time()-start
print(end)
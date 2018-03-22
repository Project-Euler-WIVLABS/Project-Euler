clear = False #1~20까지 전부다 나누어지는지 확인해보기 위한 플래그
for i in range(20,100000000000000,20): #범위설정에는 더 좋은 방법이 있을 것 같음
    for j in range(11,20):
        if i % j == 0: #현재의 i값을 1~20까지 나누면서 다 나누어지면 플래그는 true, 하나라도 안나누어지면 플래그는 false
            clear = True
        else:
            clear = False #플래그가 하나라도 false가 나오면 멈추고 i값 증가
            break
    if clear == True: #1~20까지 나눠본 후 전부다 true로 끝난 수를 뽑아내고 반복문 종료
        print(i)
        break

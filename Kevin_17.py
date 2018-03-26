def word(n):
    d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
    s=''
    if n > 999:
        s+=d[int(n/1000)]+'thousand'
    if n > 99 and n <1000:
        s+=d[int(n/100)]+'hundred'
        n=n%100
        if n > 0: s+='and'
    if n > 19 and n < 100:
        s+=d[int(n/10)*10]
        n=n%10
    if n > 0 and n < 20:
        s+=d[int(n)]
    return s
sum=0
for i in range(1,1001):
    sum += len(word(i))
print(sum)

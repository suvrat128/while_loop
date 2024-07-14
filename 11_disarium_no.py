# wap to print given no is disarium or not
### if the given no is equal to sum of individual digits to the power of its position
#### 135 =  1**1+3**2+5**3

n = int(input())
c= len(str(n))
dummy = n
summ =0
while dummy>0:
    rem=dummy%10
    dummy//=10
    summ+=(rem**c)
    c-=1
if summ == n:
    print('no is disarium')
else:
    print('no is not disarium')

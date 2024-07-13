#wap check a given number is perfect or not

n =int(input())
i=1
summ =0
while i<=n//2:
    if n%i==0:
        summ+=i
    i+=1
if summ == n:
    print('perfect')
else:
    print('not perfect')
    
#wap to find the indvisual sum of given integer

n = int(input())
summ = 0
while n > 0:
    rem = n%10
    n=n//10
    summ+=rem
print(summ)
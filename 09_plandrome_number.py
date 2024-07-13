# wap to check given number is plandrome or not

n = int(input())
rev =0
dummy = n
while dummy>0:
    rem = dummy%10
    dummy//=10
    rev = rev*10+rem
if n == rev:
    print('number is planderome')
else:
    print('not a plandrome')
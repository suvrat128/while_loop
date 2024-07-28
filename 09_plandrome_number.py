# wap to check given number is palindrome or not

n = int(input())
rev =0
dummy = n
while dummy>0:
    rem = dummy%10
    dummy//=10
    rev = rev*10+rem
if n == rev:
    print('number is palinderome')
else:
    print('not a palindrome')

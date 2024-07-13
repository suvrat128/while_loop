# wap to print the reverse of given number


n = int(input())
rev = 0
dummy = n
while dummy>0:
    rem = dummy%10
    dummy = dummy//10
    rev = rev*10+rem
print(rev)

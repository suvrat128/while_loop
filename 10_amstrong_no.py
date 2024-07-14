# wap to print given no is amstrong or not
### if the given no is equal to sum of individual digit to the power of number of digit present in a number
##### ex: 153 = 1**3+5***3+3***3

n = int(input())
dummy = n
c = len(str(n))
summ =0
while dummy>0:
   rem= dummy%10
   summ+=(rem**c)
   dummy//=10
   
if summ == n:
    print('n is an amstrong no')
else:
    print('n is not an amstrong no')
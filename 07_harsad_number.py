#wap chack given no is harshad no or not
'''
the number  which is divisible  sum of its individual digits
      ex:  12 = 1+2
        12%3==0'''


n = int(input())
summ = 0
dummy = n
while dummy>0:
    rem = dummy%10
    dummy = dummy//10
    summ+=rem
if n%summ==0:
    print('number is harshad number')
else:
    print('number is not harshad number')

#wap to find the indvisual sum of given integer

n = int(input())
summ = 0
while n > 0:
    rem = n%10
    n=n//10
    summ+=rem
print(summ)

'''
#process:
1. take int as input from user 
#5428
2. assume that the int value is 0 so summ is 0
3. using loop:
    iteration 1:
        it will take n = 5428 ,check 5428 > 0 true:
        then we fectch the last word: so rem = 5428%10 = 8 
        after that remove the last word form the n = 5428//10== 542
        and now summ = 0+8
    iteration 2:
        it will take n = 542 , check 542 >0 true:
        then we fectch the last word: so rem = 542%10 = 2 
        after that remove the last word form the n = 542//10== 54
        and now summ = 8+2
    iteration 3:
        it will take n = 54 , check 54 >0 true:
        then we fectch the last word: so rem = 54%10 = 4 
        after that remove the last word form the n = 54//10== 5
        and now summ = 10+4
    iteration 4:
        it will take n = 5 , check 5 >0 true:
        then we fectch the last word: so rem = 5%10 = 5
        after that remove the last word form the n = 5//10== 0
        and now summ = 14+5
    iteration 5:
        it will take n = 0 , check 0>0 false:
        so it will terminate the while loop
4. at after completion of loop print the summ = 19

'''
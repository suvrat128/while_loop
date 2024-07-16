#wap to check given no is prime number or not

n = int(input())

if n>1:
    
    for i in range(2,n//2+1):
        if n%i==0:
            print('no is not prinme')
            break
    else:
        print('no is prime')
        
else:
    print('no is not prime')


'''
n = 10

1. check n is greator then 1: true
    using loop:
        iteration 1:
            i = 2  so check 10%2 == 0: true
                so diret print n is not a prime and treminate the loop using break

n = 11

1. check n is greator then 1: true
    using loop:
        iteration 1:
            i = 2  so check 11%2 == 0: false go to next iteration
        iteration 2:
            i = 3 so check 11%3 == 0: false go to next iteration
        iteration 3;
            i = 4 so check 11%4 == 0: false go to next iteration
        iteration 4:
            i = 5 so check 11%5 == 0 : false go to next iteration
        loop is not grttting terminated so go to else part
    print no is prime

n = 1
1. check n is greator than 1: false
    so directly go else and print no is not a prime
'''
#using while loop:

n = int(input())
i = 2
if n>1:
    while i<n//2+1:
        if n%i==0:
            print('no is not prime')
            break
        i+=1
    else:
        print('no is prime')
else:
    print('no is not prime')

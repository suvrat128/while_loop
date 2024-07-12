# wap to print the numbers between given nuber to 10 in reverse order
'''
a=int(input())
while a>10:
    print(a)
    a-=1

#wap to print the number between given to 10
a=int(input())
while a<10:
    print(a)
    a+=1
'''
#wap to print sqare of numbers in a given range by using for loop and while loop
'''
#for loop
sl = int(input())
el = int(input())

for i in range(sl,el+1):
    print(i**2)

#while loop
sl = int(input())
el = int(input())

while sl<=el:
    print(sl**2)
    sl+=1

from where we need to start
    we will creat/initialize one variable
till where we need to go
    BY WRITING IN CONDITION
how we need to go
    either by increment or decrement'''

#wap to print fectorial of given number
a=int(input())
fact = 1
i = 1
while i<=a:
    fact*=a
    i+=1
print(fact)

    
    

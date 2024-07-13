#wap to print sqare of numbers in a given range by using for loop and while loop

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

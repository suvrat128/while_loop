While loop: 
1. We use while loop when we are not sure how many times we have to iterate.
2. While loop will be executed based on one condition
3. There is a chance to execute ur while loop for infinite times, in order to avoid that make sure at one point of time the condition become false

Syntax:
	
     while condition:
		    statments of
		    while block


Process of extract individual digits of a given number:
1. Divide the given number with 10 and get reminder (so last digit we will extract)
2. As we have extracted last digit so we will reduce the number so we can delete last digit by re assigning the number value by dividing the given with 10
3. The above two step has to be repeated till n is greater than 0 (/so we will use while loop)

example:

#wap to find the indvisual sum of given integer

	n = int(input())
	summ = 0
	while n > 0:
		rem = n%10
    	n=n//10
    	summ+=rem
	print(summ)

 Special statements of loop:
 
1. break
   
	It is used for terminating the execution of loop
	Break can be used with both for and while loop

First operation after that breaking the loop
Using while loop:

	a=1
	While a<11:
 	print(a)
	if a==5:
	     break
	a+=1
 First breaking next operation

 	a=1
	While a<11:
	if a==5:
	     break
	print(a)
	a+=1

 2. continue:

It is used for skipping current iteration of loop

Ex: using for loop

	For I in range(1,11):
	if I==5:
		continue
	print(I)

Ex: using while loop
	
 	a=1
	While a<11:
	if a==5:
		a+=1
		continue
	print(a)
	a+=1

3. pass:
   
1. Pass is used for creating empty blocks without any errors 
2. This empty block can be used for writhing code in features
3. Pass can be used with if, for , while, function, class, method

ex1:
	
 		If 1>0:
		pass
ex2:

		For I in range(1,11):
		pass
ex3:

		Def hai()
		pass




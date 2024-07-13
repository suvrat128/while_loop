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

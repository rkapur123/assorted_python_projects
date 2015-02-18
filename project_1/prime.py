__author__ = 'RahulKapur'

#Rahul Kapur
#rk2749

x = int(input("Enter a number ")) #take an input from the user
check = 0
if x <= 1: #if number is less than or equal to 1
    print str(x) + ' is not prime' #it is not prime
else: #if greater than one
    for z in range(2, x): #loop from 2 on to x
        if (x%z) == 0: #check remainder
            check = 1 #is not prime

    if check == 1:
        print str(x) + " is not prime" #print is not
    else:
        print str(x) + " is prime" #print is prime

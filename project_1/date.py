__author__ = 'RahulKapur'
#Rahul Kapur
#rk2749

from datetime import date #import function dat from datetime

a = int(input("What year were you born in? "))#store integer values
b = int(input("Which month of the year? (1,2,3...12) "))
c = int(input("Which day were you born? "))
birthDate = date(a,b,c) #create a date object
currentDate = date.today() #find todays date
difference = currentDate - birthDate #subtract the two objects
print("The number of days since you were born " + str(difference.days)) #print the answer
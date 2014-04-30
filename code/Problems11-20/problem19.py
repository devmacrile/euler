#Devin Riley
#Project Euler
#Problem 19
#1/6/2013

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time

monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = time.time()

day  = 2
first_sundays = 0

#i is year, k is month; loop through each
for i in range(1900, 2001):#each year
    monthdays [1] = 28
    days = 365
    if i % 4 == 0 and i != 2000:
        days = days + 1 #leap year
        monthdays [1] = 29
    day = day%days
    for k in range(1,13):#each month
        day = day + 7 - monthdays[k-1]
        while day <= monthdays[k-1]:
            day += 7
        if day - monthdays[k-1] == 1 and i > 1900:
            first_sundays += 1
            
            
        
elapsed = time.time() - start    
print "The number of Sundays that fell on the first day of the month in the 20th century is %s, which was found in %s seconds using the above method." %(first_sundays, elapsed)


# The number of Sundays that fell on the first day of the month in the 20th century is 171, which was found in 0.00202798843384 seconds using the above method.

#also note Gauss has a cool formula for the calculation of the day of the week of January 1st for any given year which can be extended for more general purposes: http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Formulas_derived_from_Gauss.27s_algorithm













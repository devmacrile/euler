#Devin Riley
#Project Euler
#Problem 20
#1/2/14

"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

###library imports
import time

###functions
def factorial(n):
    #returns the factorial of integer n
    if n == 1 or n == 0:
        return n
    return n*factorial(n-1)

def sum_of_digits(n):
    #originally from problem 16!  
    #returns sum of digits of an integer n
    result = 0
    tracker = n
    while(tracker > 0):
        result += tracker % 10
        tracker = (tracker - tracker%10)/10
    return result
 
   
   
###calcs
start = time.time()
bignumber = factorial(100)
result = sum_of_digits(bignumber)
elapsed = time.time() - start

print "The answer is %s, which was doable in %s seconds." (%result, elapsed)



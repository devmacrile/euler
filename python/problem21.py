#Devin Riley
#Project Euler
#Problem 21
#1/26/14

""" 
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

###library imports
import time

###functions
def sumOfDivisors(n):
    result = 0
    for i in range(1, n/2 + 1):
        if n%i == 0:
            result += i
    return result
        
   
start = time.time()   

answer = 0
for i in range(1,10000):
    divsum = sumOfDivisors(i)
    if i != divsum and i == sumOfDivisors(divsum):
        #print i, " ", divsum
        answer += i
    
elapsed = time.time() - start

print "The sum of all amicable numbers under 10000 is %s, found in %s seconds" %(answer, elapsed)

#The sum of all amicable numbers under 10000 is 31626, found in 3.9666159153 seconds
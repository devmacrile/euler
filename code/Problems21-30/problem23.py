#Devin Riley
#Project Euler
#Problem 23
#1/28/2014

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of 
two abundant numbers is 24.  By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers.  However, this upper limit cannot be reduced any further by analysis even 
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

#so between 24 and 28123
#are sums of abundant numbers abundant?

###library imports
import time


###functions
def sumOfDivisors(n):
    result = 0
    for i in range(1, n/2 + 1):
        if n%i == 0:
            result += i
    return result
    
def isAbundant(n):
    if sumOfDivisors(n) > n:
        return True
    else:
        return False



#calculate abundant numbers, write them to file
abundantNumbers = []
"""
for i in range(1, 28124):
    if sumOfDivisors(i) > i:
        abundantNumbers.append(i)

f = open("abundants.txt", "w")
for ab in abundantNumbers:
    f.write("%s\n" % ab)
f.close()
"""

##read abundant numbers from file
with open('abundants.txt') as f:
    abundantNumbers = f.read().splitlines()
f.close()

#convert string literals into ints
for i in range(0, len(abundantNumbers)):
    abundantNumbers[i] = int(abundantNumbers[i])


###let's do this
start = time.time()
numAbundants = len(abundantNumbers)
answer = 0
limit = 28124
isSumAbundant = [False for i in range(limit)]


for i in range(numAbundants):
    for j in range(i, numAbundants):
        if abundantNumbers[i] + abundantNumbers[j] <= limit:
            isSumAbundant[abundantNumbers[i] + abundantNumbers[j] - 1] = True
        else:
            break
            
for i in range(len(isSumAbundant)):
    if not isSumAbundant[i]:
        answer += i + 1


elapsed = time.time() - start        
print "The solution is %s, found in %s seconds." %(answer, elapsed)

#The solution is 4179871, found in 6.28140616417 seconds.



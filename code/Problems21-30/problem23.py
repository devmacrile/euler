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

print sumOfDivisors(64)
print isAbundant(64)


###variables
start = time.time()
abundantNumbers = []
answer = 0
flag = False

###main calculation
for i in range(1, 28123+1):
    if sumOfDivisors(i) > i:
        abundantNumbers.append(i)

a=False
# vv is an interesting series; seems like there is some pattern.. plot in R?
for i in abundantNumbers:
    a= False
    if i %2 ==0 and i%3 ==0:
        a = True
    print i, " ", a
    if i > 1000:
        break
print len(abundantNumbers)

#NONE!!!! so all abundant numbers are divisible by 2 or 3 (intuitively)
for i in abundantNumbers:
    if i%2 != 0 and i%3 != 0:
        print "Hey! ", i

for i in abundantNumbers:
    print i
    if i > 100:
        break

for i in range(len(abundantNumbers)):
    print abundantNumbers[i+1] - abundantNumbers[i]
    if abundantNumbers[i] > 100:
        break
"""
for i in range(1,28123+1):
    if i < 50 or i%2 == 1:
        print i
        for j in abundantNumbers:
            flag = False
            if i - j in abundantNumbers:
                print i, " ", j, " ", i-j
                flag = True
                break
    if not flag:
        answer += i
       
elapsed = time.time() - start        
print "The solution is %s, found in %s seconds." %(answer, elapsed)
    
    
    """
    
    
    
    
    
    
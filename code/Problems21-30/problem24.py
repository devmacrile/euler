#Devin Riley
#Project Euler
#Problem 24
#5/1/14


"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

#initial thoughts:
#Ways to permute 10 numbers = 10!
#approach: what 9! chunk is 1000000 in?
#           what 8! chunk?
#            what 7! chunk?
#             ......
 
import time
import math

def factorial(n):
    #returns n!
    if n < 0:
        print "ERROR: cannot compute factorial of a negative number"
        return
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

start = time.time()
n = 10 #for digits 0-9    
#print factorial(n)
#3,628,800
digs = range(0,n)
answer = 0
remainder = 1000000.0
for i in range(n):
    j = len(digs)
    factbin = int(math.ceil(remainder/factorial(j-1)))
    dig = digs[factbin - 1]
    remainder -= (factbin-1) * factorial(j-1)
    answer *= 10 #add new digit
    answer += dig #to 10s place of answer
    digs.remove(dig) #remove digit list to permute

answer = int(answer)
elapsed = time.time() - start

print "The solution is %s, found in %s seconds." %(answer, elapsed)
#




#Devin Riley
#Project Euler
#Problem 24
#2/9/14


"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

#initial thoughts:
#Ways to permute 10 numbers = 10!
 
def factorial(n):
    #returns n!
    if n == 1:
        return n
    return n*factorial(n-1)
    
print factorial(10)
#3,628,800

#9! that start with 1, 9! that start with 2, etc.
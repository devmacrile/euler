"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

"""
Initial thoughts:
Ways to permute 10 numbers = 10!
approach: what 9! chunk is 1000000 in?
           what 8! chunk?
            what 7! chunk?
             ......
"""
 
import math

from eutil import clock

@clock
def main():   
    digits = range(10)  # 0-9
    answer = 0
    remainder = 1000000.0
    for i in range(10):
        j = len(digits)
        fact = math.factorial(j - 1)
        factbin = int(math.ceil(remainder/fact))
        digit = digits[factbin - 1]
        remainder -= (factbin-1) * math.factorial(j-1)
        answer *= 10  # add new digit
        answer += digit  # to 10s place of answer
        digits.remove(digit)  # remove digit list to permute 
    return int(answer)


if __name__ == '__main__':
    main()




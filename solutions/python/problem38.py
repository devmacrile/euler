# -*- coding: utf-8 -*-
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

"""
Solve this more or less by space reduction.
First, we note that 9 itself produces a pandigital with n = 4, 
which gives us a nice benchmark of 918273645.  Next, we note that
no two digit 'seed' (e.g. 192 in the example above) can produce a pandigital
result (>95 => nine is duplicated in the second iteration, similar reasoning
for each of 91, 92, etc.).  And, on the other hand, the seed cannot have 
more than four digits, else there's no way to have n>1.  Thus, we have a 
three or four digit seed that must be greater than 9182 (the first four 
digits of the seed 9 benchmark).

Noting that the number must start with a 9, we know that for seed*2
we will wind up with the leading digits '18' (so seed cannot have either a 1 or an 8
in it), and the larger the seed the further to the right this '18' will be placed.  
So the largest pandigital will have a four digit seed starting with nine (and through 
similar reasoning as above, must have a number <5 as the second digit).  Thinking there
is probably a more elegant recursive enumeration here, but good enough for me to brute 
force at this point ((6 choose 3) * 3! = 120 possibilities).
"""

import itertools

from eutil import clock

VALID_DIGITS = '234567'


def is_pandigital(n):
    digit_set = set([digit for digit in str(n)])
    nine_distinct = len(digit_set) == 9
    no_zeros = '0' not in digit_set
    return (nine_distinct and no_zeros)

@clock
def main():
    pandigitals = []
    for permutation in itertools.permutations(VALID_DIGITS, 3):
        seed = '9' + ''.join(permutation)
        candidate = seed + str(int(seed) * 2)
        if is_pandigital(candidate):
            pandigitals.append(int(candidate))
    return max(pandigitals), len(pandigitals)


if __name__ == '__main__':
    main()

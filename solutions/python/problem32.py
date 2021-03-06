# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, the 5-digit number, 
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools

from eutil import clock

DIGITS = ''.join(map(str, range(1,10)))


def evaluate(digits):
    """
    Products will always be 4 digits long, so limits the splits we need to evaluate.
    """
    products = []
    x = ''.join(digits)
    for n in range(2, 5):
        product = int(x[:n]) * int(x[n:5])
        if product == int(x[5:]):
            return True, product
    return False, None


@clock
def main():
    sums = set()
    for perm in itertools.permutations(DIGITS, len(DIGITS)):
        checks_out, product = evaluate(perm)
        if checks_out:
            sums.add(product)
    return sum(sums)


if __name__ == '__main__':
     main()

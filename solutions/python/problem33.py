# -*- coding: utf-8 -*-
"""
The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""

from operator import mul

from eutil import clock


def truncate(n):
    """
    Makes the last digit of n 0
    """
    return 10 * (n // 10)

def conditions(i, j):
    fraction = float(i) / j
    conds = (fraction == (float(truncate(i) / 10) / float(j % 10)),
             (i % 10) == float(truncate(j) / 10))
    return all(conds)

def generate_pairs():
    x = [x for x in range(10, 100) if (x % 10) > 0]
    return [(i, j) for i in x for j in x if i < j] 

@clock
def main():
    numerators = 1
    denominators = 1
    pairs = generate_pairs()
    for i, j in pairs:
        if conditions(i, j):
            numerators *= i
            denominators *= j
    return int(1. / (float(numerators) / denominators))


if __name__ == '__main__':
    main()

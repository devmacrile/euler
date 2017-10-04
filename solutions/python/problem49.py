# -*- coding: utf-8 -*-
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms 
are prime, and, (ii) each of the 4-digit numbers are permutations of 
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
primes, exhibiting this property, but there is one other 4-digit 
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import itertools

from eutil import clock, primes


def is_permutation(x, y):
    return sorted(str(x)) == sorted(str(y))


@clock
def main():
    diff = 3330
    seen = set([1487, 4817, 8147])
    primeset = set(primes(10000))
    for p in primes(10000):
        if (p < (1000 + diff)) or ('0' in str(p)) or (p in seen):
            continue
        if (p - diff) in primeset and (p + diff) in primeset:
            if is_permutation(p, p - diff) and is_permutation(p, p + diff):
                return ''.join(map(str, [p - diff, p, p + diff]))
    return None


if __name__ == '__main__':
    main()
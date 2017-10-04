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
import collections

from eutil import clock, primes


@clock
def main():
    seen = [1487, 4817, 8147]
    pset = set(primes(10000))
    for p in pset:
        if p < 1000 or '0' in str(p):# or p in seen :
            continue
        perms = set([int(''.join(perm)) for perm in itertools.permutations(str(p), 4)])
        are_prime = [perm in pset for perm in perms]
        if p == 1487:
            print('-------- WOOOOOO \n\n')
            print(collections.Counter(are_prime)[True])

        if collections.Counter(are_prime)[True] >= 3:
            print(are_prime)
            print(p, sorted([p for i, p in enumerate(perms) if are_prime[i] is True]))
            #return ''.join(sorted([str(p) for i, p in enumerate(perms) if are_prime[i]]))


if __name__ == '__main__':
    main()
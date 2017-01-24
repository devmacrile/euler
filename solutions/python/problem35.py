# -*- coding: utf-8 -*-
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from eutil import clock, sieve


valid_digits = ['1', '3', '7', '9']
primes = set(sieve(1000000))

@clock
def main():
    cache = set()
    for prime in primes:
        if prime not in cache and not (prime > 10 and not all([x in valid_digits for x in str(prime)])):
            rotations = set([int(str(prime)[n:] + str(prime)[:n]) for n in range(len(str(prime)))])
            if all([r in primes for r in rotations]):
                for r in rotations:
                    cache.add(r)
    return len(cache)


if __name__ == '__main__':
    main()

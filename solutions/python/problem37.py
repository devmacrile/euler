# -*- coding: utf-8 -*-
"""
The number 3797 has an interesting property. Being prime itself, it is 
possible to continuously remove digits from left to right, and remain 
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from 
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from eutil import clock, sieve, is_prime

def truncatable(n):
    return left_truncatable(n) and right_truncatable(n)

def left_truncatable(n):
    if n // 10 == 0:
        return is_prime(n)
    return is_prime(n) and left_truncatable(int(str(n)[1:]))

def right_truncatable(n):
    if n // 10 == 0:
        return is_prime(n)
    return is_prime(n) and right_truncatable(int(str(n)[:-1]))

@clock
def main():
    truncatables = []
    prime_gen = sieve(10000000)  # arbitarily high
    while len(truncatables) < 11:
        prime = next(prime_gen)
        if prime < 10:
            continue
        if truncatable(prime):
            truncatables.append(prime)
    print truncatables
    return sum(truncatables)


if __name__ == '__main__':
    main()

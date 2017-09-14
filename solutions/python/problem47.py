# -*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors 
each. What is the first of these numbers?
"""

from eutil import clock, distinct_prime_factors


@clock
def main():
    prime_factor_counts = distinct_prime_factors(1000000)

    consecutive = 0
    for i, count in enumerate(prime_factor_counts):
        if count == 4:
            consecutive += 1
            if consecutive == 4:
                break
        else:
            consecutive = 0

    return (i - consecutive + 1)



if __name__ == '__main__':
    main()
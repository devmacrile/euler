# -*- coding: utf-8 -*-
"""
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

 9 = 7 + 2 × 1^2
15 = 7 + 2 × 2^2
21 = 3 + 2 × 3^2
25 = 7 + 2 × 3^2
27 = 19 + 2 × 2^2
33 = 31 + 2 × 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?
"""

import math

from eutil import clock, prime_index


def prime_square_sum(x, primes, squares):
    for square in squares:
        if primes[x - 2 * square]:
            return True
    return False


def next_square(square):
    next_root = math.sqrt(square) + 1
    return int(math.pow(next_root, 2))


@clock
def main():
    squares = [x * x for x in range(10)]  # arbitrary initialization
    prime_flags = prime_index(10000)  # 'guess' at upper bound

    i = 1

    while True:
        i += 2
        if prime_flags[i]:
            continue

        if i > squares[-1]:
            new_square = next_square(squares[-1])
            squares.append(new_square)

        if prime_square_sum(i, prime_flags, squares):
            continue

        return i


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. For example, 2143 is 
a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

"""
Main insight is remembering that if the sum of a numbers
digits is a multiple of three, so is the number itself.
Thus, only two of the digit lengths for the n-digit 
pandigitals are valid.

Here, also utilized the Miller-Rabin probabilistic primality
test for a speed boost (though depends on the number of misses
in the pandigitals since were still using the slow is_prime
for confirmation).
"""

from itertools import permutations

from eutil import clock, miller_rabin_test


@clock
def main():
    valid_n = [x for x in range(2, 10) if sum(range(x + 1)) % 3 != 0]
    for n in reversed(sorted(valid_n)):
        digits = ''.join(map(str, range(1, n + 1)))
        pandigitals = reversed(sorted([''.join(p) for p in permutations(digits, n)]))
        for pandigital in pandigitals:
            candidate = int(pandigital)
            if miller_rabin_test(candidate, 40):
                if is_prime(candidate):
                    return candidate
    return None


if __name__ == '__main__':
    main()
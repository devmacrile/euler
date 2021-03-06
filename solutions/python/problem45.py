# -*- coding: utf-8 -*-
"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

"""
- By observation and a test, hexagonal numbers are a subset of triangle numbers.
- Solve the equation for pentagonal numbers for n in terms of x.  Then for a
  given x, if this new equation provides an integer then it is pentagonal.
"""

import math

from eutil import clock

triangle = lambda x: x * (x + 1) // 2
pentagonal = lambda x: x * (3 * x + 1) // 2
hexagonal = lambda x: x * (2 * x - 1)

def is_pentagonal(x):
    inverse = float(1 + math.sqrt(24 * x + 1)) / 6
    return inverse.is_integer()

@clock
def main():
    solution = None
    hindex = 143
    while True:
        hindex += 1
        candidate = hexagonal(hindex)
        if is_pentagonal(candidate):
            solution = candidate
            break
    return solution


if __name__ == '__main__':
    main()
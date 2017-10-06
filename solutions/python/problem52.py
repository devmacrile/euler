# -*- coding: utf-8 -*-
"""
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
and 6x, contain the same digits.
"""

import itertools

from eutil import clock


def digset(n):
    return set(list(str(n)))


@clock
def main():
    solution = None
    for candidate in range(1, 1000000):
        if digset(candidate) == digset(2 * candidate) == \
           digset(3 * candidate) == digset(4 * candidate) == \
           digset(5 * candidate) == digset(6 * candidate):
           solution = candidate
           break
           
    return solution


if __name__ == '__main__':
    main()
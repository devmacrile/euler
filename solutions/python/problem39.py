# -*- coding: utf-8 -*-
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math
from collections import defaultdict

from eutil import clock


def cache_string(numbers):
    return ','.join(map(str, sorted(numbers)))

@clock
def main():
    solutions = defaultdict(int)
    cache = set()
    for a in xrange(1, 500):
        for b in xrange(1, 500):
            cstring = cache_string([a, b])
            if cstring in cache:
                continue
            c = math.sqrt(a ** 2 + b ** 2)
            if (a + b + c) > 1000:
                break
            if c.is_integer():
                solutions[(a + b + int(c))] += 1
                cache.add(cstring)
    return max(solutions.iterkeys(), key=(lambda key: solutions[key]))

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math
import itertools
from collections import Counter

from eutil import clock


max_digit = {2: 5, 3: 7, 4: 8, 5: 9}
factorials = map(math.factorial, range(0, 10))

@clock
def faster():
    result = 0
    for i in range(2, 6):
        digits = ''.join(map(str, range(max_digit.get(i, 10))))
        for j in itertools.combinations_with_replacement(digits, i):
            sum_digit_factorials = sum([factorials[int(x)] for x in j])
            if Counter(j) == Counter([x for x in str(sum_digit_factorials)]):
                result += sum_digit_factorials
    return result

@clock
def main():        
    return sum([n for n in range(3, 100000) if n == sum([factorials[int(x)] for x in str(n)])])

if __name__ == '__main__':
    faster()
    main()

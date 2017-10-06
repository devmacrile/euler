# -*- coding: utf-8 -*-
"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 
is almost unimaginably large: one followed by two-hundred zeros. Despite their 
size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the 
maximum digital sum?
"""

from eutil import clock


@clock
def main():
    upper_bound = 100
    max_sum = 0
    for a in range(1, upper_bound):
        for b in range(1, upper_bound):
            absum = sum([int(d) for d in str(pow(a, b))])
            if absum > max_sum:
                max_sum = absum
                solution = (a, b, absum)
    return solution


if __name__ == '__main__':
    main()
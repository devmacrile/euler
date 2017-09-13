# -*- coding: utf-8 -*-
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
of each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2 d3 d4  =  406 is divisible by 2
d3 d4 d5  =  063 is divisible by 3
d4 d5 d6  =  635 is divisible by 5
d5 d6 d7  =  357 is divisible by 7
d6 d7 d8  =  572 is divisible by 11
d7 d8 d9  =  728 is divisible by 13
d8 d9 d10 =  289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from collections import Counter

from eutil import clock


DIGIT_SET = set(map(str, range(10)))

def multiples(n, upper_bound=1000):
    """
    Returns str representation of multiples of `n` that are
    less than `upper_bound` and whose digits are all unique
    """
    multiples = []
    for i in xrange((upper_bound // n) + 2):
        if (n * i) < 100:
            digits = '0' + str(n * i)
        else:
            digits = str(n * i)

        if len(set(digits)) < 3:
            continue

        multiples.append(digits)

    return multiples


def interlock_integers(m1, m2):
    """E.g. 428 and 289 interlock with digits '28'"""
    cond1 = lambda x, y: x[1:] == y[:2]
    cond2 = lambda x, y: x[0] not in set(y[2:])
    return [(x[0] + y) for x in m2 for y in m1 if cond1(x,y) and cond2(x,y)]


def enumerate_candidates(divisors, candidates):
    if len(candidates) == 0:
        n = divisors[0]
        return enumerate_candidates(divisors[1:], multiples(n))
    elif len(divisors) == 0:
        return candidates
    else:
        n = divisors[0]
        rest = divisors[1:]
        extended_candidates = interlock_integers(candidates, multiples(n))
        return enumerate_candidates(rest, extended_candidates)

@clock
def main():
    divisors = [17, 13, 11, 7, 5, 3, 2]
    candidates = enumerate_candidates(divisors, [])
    missing_digit = lambda x: DIGIT_SET.difference(set(x)).pop()
    pandigitals = [int(missing_digit(x) + x) for x in candidates]
    return sum(pandigitals), pandigitals


if __name__ == '__main__':
    main()
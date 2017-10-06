# -*- coding: utf-8 -*-
"""
By replacing the 1st digit of the 2-digit number *3, it turns 
out that six of the nine possible values: 13, 23, 43, 53, 73, 
and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among 
the ten generated numbers, yielding the family: 56003, 56113, 56333, 
56443, 56663, 56773, and 56993. Consequently 56003, being the first 
member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.
"""

from itertools import combinations

from eutil import clock, sieve, is_prime


@clock
def main():
    n = 1000000
    pset = set(list(sieve(n)))
    # set is unordered, but assuming there is
    # only one family under our upper bound assumption
    for p in pset:
        num_digits = len(str(p))
        for replacement_size in range(1, num_digits):
            digit_place_combos = combinations(range(num_digits), replacement_size)
            for digit_places in digit_place_combos:
                family_members = []
                for digit in ''.join(map(str, range(10))):
                    digit_list = list(str(p))
                    for digit_place in digit_places:
                        digit_list[digit_place] = digit
                    candidate = int(''.join(digit_list))
                    if digit_list[0] != '0' and candidate in pset:
                        family_members.append(candidate)
                if len(family_members) == 8:
                    return min(family_members)
    return None


if __name__ == '__main__':
    main()
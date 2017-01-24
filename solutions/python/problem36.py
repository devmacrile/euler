# -*- coding: utf-8 -*-
"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


Only odd numbers are possible (otherwise, complement includes leading 0).
TODO: generate the base ten palindromes instead of iterating over odd numbers.
"""

from eutil import clock


def is_palindrome(s):
    return [x for x in s] == [x for x in reversed(s)]

@clock
def main():
    return sum([x for x in range(1, 1000000, 2) if is_palindrome(str(x)) and is_palindrome(bin(x)[2:])])

                
if __name__ == '__main__':
    main()

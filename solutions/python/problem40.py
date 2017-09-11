# -*- coding: utf-8 -*-
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from eutil import clock

@clock
def main():
    digits = ''.join([str(i) for i in range(1, 200000)])  # 200000 arbitrary, get's us to 1000000 digits
    subdigits = map(int, [digits[0], digits[9], digits[99], digits[999], digits[9999], digits[99999], digits[999999]])
    return reduce(lambda a, b: a * b, subdigits)

if __name__ == '__main__':
    main()
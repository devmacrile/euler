# -*- coding: utf-8 -*-
"""
It is possible to show that the square root of two can be expressed as an 
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393/985, is the first example where the number of digits in the 
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than denominator?
"""

"""
Numerators follow 3, 7, 17, 41, 99, 239, 577...
Denominators follow 2, 5, 12, 29, 70, 169, 408...
Which gives us a sequence relationship:
    Next numerator will be the sum of the current numerator and the product of two
        and the current denominator
    Next denominator will be the sum of the current denominator and the current
        numerator.
"""

from eutil import clock


@clock
def main():
    solution = 0
    n, d = 1, 1
    for i in range(1000):
        n, d = n + 2 * d, d + n
        if len(str(n)) > len(str(d)):
            solution += 1
    return solution


if __name__ == '__main__':
    main()
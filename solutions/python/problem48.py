# -*- coding: utf-8 -*-
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
"""
10:   0405071317
100:  9027641920
1000: 9110846700

Only real optimization is that we only care about the last ten digits
of the sum, so can take the self power % 10^10 for each, which reduces
the overhead of having a monstrous number.
"""

from eutil import clock


@clock
def main():
    s = sum([pow(x, x, 10**10) for x in range(1, 1001)])
    return str(s)[-10:]


if __name__ == '__main__':
    main()
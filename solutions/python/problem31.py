# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

from eutil import clock

def next_denomination(n):
    denoms = {200: 100, 100: 50, 50:20, 20:10, 10:5, 5:2, 2:1}
    return denoms[n]

def count_partitions(amount, max_denomination):
    if amount < 5 or max_denomination <= 1:
        return 1
    else:
        partitions = 0
        n = 0
        while (amount - n * max_denomination) >= 0:
            partitions += count_partitions(amount - n * max_denomination, next_denomination(max_denomination))
            n += 1
    return partitions

@clock
def main():
    return count_partitions(200, 200)

if __name__ == '__main__':
    main()

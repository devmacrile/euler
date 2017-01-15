"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


from eutil import clock


def diagonal_generator(seed, max_value):
    level = 1
    current_value = seed
    yield seed  # initially yield the single center value
    while current_value < max_value:
        for i in range(4):
            next_value = current_value + (2 * level)
            yield next_value
            current_value = next_value
        level += 1


@clock
def main():
    total = 0
    gen = diagonal_generator(1, 1001 ** 2)
    for x in gen:
        total += x
    return total


if __name__ == '__main__':
    main()

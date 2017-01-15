"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

"""
Brute-force on this solution (only takes ~1.5 seconds).

Observations that could be utilized for more efficiency:
  - The sum of the digit powers will be cyclical, and will have a bounded cycle
    for each size of digit (i.e. 4-digit numbers will have a cycling upper/lower bounds),
    so can reduce search space (equivalent to checking all combinations of 0-9 for each digit size).
  - f(x) = sum_of_digit_5th_powers(x) will diverge from the identity function f(x) = x,
    and so there is a hard upperbound on possible answers (this is utilized below).
"""

from eutil import clock


def sum_of_digit_powers(x, power=5):
    return sum(map(lambda y: int(y) ** power, str(x)))

@clock
def main():
    return sum([x for x in range(sum_of_digit_powers(99999)) if sum_of_digit_powers(x) == x and x > 1])
            

def plot(sequence, power=4, identity=True):
    import matplotlib.pyplot as plt
    plt.plot(sequence, [sum_of_digit_powers(x) for x in sequence], color='b')
    if identity:
        plt.plot(sequence, sequence, color='r')
    plt.show()

if __name__ == '__main__':
    #plot(range(30000), power=4)
    main()

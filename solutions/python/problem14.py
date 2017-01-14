"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import operator
from collections import defaultdict

from eutil import clock, collatz_sequence


@clock
def brute():
    result = 0
    value = 1000000
    for i in range(1000000):
        j = i
        count = 0
        while j > 1:
            count = count + 1
            if j % 2 == 0:
                j = j/2
            else:
                j = 3*j + 1
        if count > result:
            result = count
            value = i
    return value


@clock
def main(upper_bound=1000000):
    """
    Search-space reducing insights:
       - Solution must be > 500k, else double it and you have a longer sequence.
       - Solution cannot have come from 3n + 1 operation by same reasoning, so
         the inverse of this operation must be even for the solution (and thus,
         would have been cut by two instead by definition).
       - Many numbers will be part another's sequence, so cache these calculations.

    TODO: Turns out, the 500k+ 'optimization' slows things down ~2x.  Must be the 
    interaction with the cached results, but would be interesting to figure this out.
    """
    seqlens = defaultdict(lambda: 0)
    even_inverse = lambda x: ((float(x - 1) / 3) % 2) == 0.0
    candidates = [x for x in range(1, upper_bound, 2) if even_inverse(x)]
    for candidate in candidates:
        num = candidate
        while num > 1:
            seqlens[candidate] += 1
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            if num in seqlens:
                seqlens[candidate] += seqlens[num]
                break
    answer = max([k for k in seqlens], key=(lambda key: seqlens[key]))
    return answer, seqlens[answer]


def plot_solution_sequence():
    import matplotlib.pyplot as plt
    solution, length = main()
    plt.plot(range(length), list(collatz_sequence(solution)), label='start = %s' % str(solution))
    plt.title('Longest Collatz Sequence (n < 1000000)')
    plt.xlabel('Iteration')
    plt.ylabel('Sequence value')
    plt.legend(loc='upper right')
    plt.show()
    
        
if __name__ == '__main__':
    #brute()  # for performance comparison
    main()

    # Plot is kind of cool, showing the sequence
    # to be a kind of temporal fractal
    plot_solution_sequence()

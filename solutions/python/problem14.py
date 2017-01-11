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

from eutil import clock


@clock
def main():
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
        
if __name__ == '__main__':
    main()

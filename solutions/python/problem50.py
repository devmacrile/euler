# -*- coding: utf-8 -*-
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 
21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
""" 

"""
The relationship between the longest chain of primes that
sum to a prime (say, k) and the upper bound prime (say, n)
is s.t. multiplying n by 10 approximately triples the length
of the longest chain:

For n = 10, k = 2
For n = 100, k = 6
For n = 1000, k = 21
For n = 10000, k = 65
For n = 100000, k = 183
...
So for n=1e6, k~540, which means the average value
in the chain must be < ~2000, and so we can choose
a safe but reasonable upper bound to limit the search 
space for the chain (say, 5000; though could  probably
prove something more formally).
"""

from eutil import clock, primes, is_prime


@clock
def main():
    n = 10
    primelist = primes(5000)
    longest = []
    for i in range(len(primelist)):
        for j in range(i + len(longest), len(primelist)):
            if sum(primelist[i:j]) > n:
                break
            if (j - i) > len(longest):
                if is_prime(sum(primelist[i:j])):
                    longest = primelist[i:j]
    return len(longest), sum(longest)


if __name__ == '__main__':
    main()
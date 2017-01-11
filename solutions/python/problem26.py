"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit 
fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen 
that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its 
decimal fraction part.

Insight:  the period of 1/p is equal to the order of 10 mod p.
"""

from eutil import clock, sieve

    
def prime_period(p):
    """
    Find the x s.t. pow(10, x) % p == 1
    """
    for i in range(1, p):
        if 10**i % p == 1:
            return i
    return 0


@clock
def main():
    primes = list(sieve(1000))
    max_period = max(prime_period(x) for x in primes)
    result = [x for x in primes if prime_period(x) == max_period][0] 
    return result


if __name__ == '__main__':
    main()

    
    


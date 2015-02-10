#Devin Riley
#Project Euler
#10/2/2014
#Problem 26

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
"""

"""
The period of 1/p is equal to the order of 10 mod p
"""

#libraries
import time

#functions
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes
    
def prime_period(p):
	# find x such that 10**x % p == 1
	for i in range(1, p):
		if 10**i % p == 1:
			return i
	return 0

#calculation
start = time.time()
primes = primes_sieve(1000)
max_period = max(prime_period(x) for x in primes)
result = [x for x in primes if prime_period(x) == max_period][0]   
elapsed = time.time() - start

print "The answer is %s, which was found in %s seconds" %(result, elapsed)
#The answer is 983, which was found in 0.298069953918 seconds

    
    


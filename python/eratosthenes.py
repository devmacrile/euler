#Implementation of the Sieve of Eratosthenes
#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Used in:
# 26

import math

def sieve(n):
	ints = [True] * n
	ints[0] = ints[1] = False
	
	for (i, isprime) in enumerate(ints):
		if isprime:
			yield i
			for n in xrange(i*i, n, i):
				ints[n] = False

def sieveOfEratosthenes(n):
	g = sieve(n)
	primes = list(g)
	return primes
	
if __name__ == '__main__':
	main()
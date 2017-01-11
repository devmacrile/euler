"""
A collection of utility functions used by python solutions in this directory.
"""

import time
import functools
import math


def clock(func):
    """
    Utilized to time solutions and display answer.
    """
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def memoize(function):
    """
    Cache function calls for arguments.
    Useful for problems with repeated/recursive calculations.
    """
    memo = {}

    @functools.wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


def sieve(n):
    """
    Generator to return primes using the sieve of eratosthenes.
    """
    ints = [True] * n
    ints[0] = ints[1] = False	
    for (i, isprime) in enumerate(ints):
        if isprime:
            yield i
            for n in xrange(i*i, n, i):
                ints[n] = False


def primes(n):
    """
    Return a list of primes less than n.
    """
    pgen = sieve(n)
    return list(pgen)


@memoize
def sum_of_divisors(n):
    """
    Computes the sum of the divisors of n.
    """
    result = 0
    for i in range(1, n/2 + 1):
        if (n % i) == 0:
            result += i
    return result

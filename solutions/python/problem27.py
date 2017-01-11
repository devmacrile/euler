"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 
primes for the consecutive values n = 0 to 79. The product of the coefficients, 
-79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000	

where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |-4| = 4).

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting 
with n = 0.
"""

"""
Key insights:

- Primes are not necessarily unique
- Both functions given are the same, just shifted.
- Longest curve s.t. |a|,|b| < 1000 will also be along this curve,
  so just need to find first prime under 1000 (as a function of increasing
  n) to solve for b, and use the next prime on the curve, say y, to 
  solve for a:  1^2 + a*n + b = y.
"""

from eutil import clock


remarkable = lambda n: (n*n + n + 41)
incredible = lambda n: (n*n - 79*n + 1601)

def plots():
    import matplotlib.pyplot as plt
    plt.plot(range(41), map(remarkable, range(41)), color='b', label='Remarkable')
    plt.plot(range(80), map(incredible, range(80)), color='g', label='Incredible')
    plt.legend(loc='upper left')
    plt.show()


@clock
def main():
    incredibles = map(incredible, range(80))
    for i, wow in enumerate(incredibles):
        if wow < 1000:
            b = wow
            index = i
            break
    a = (incredibles[i + 1] - 1) - wow
    return (a * b)
    
if __name__ == '__main__':
    main()
    plots()
    
    


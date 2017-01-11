"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of 
two abundant numbers is 24.  By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers.  However, this upper limit cannot be reduced any further by analysis even 
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

[So, between 24 and 28123.  Q: are sums of abundant number abundant?]
"""

from eutil import clock, sum_of_divisors

    
def is_abundant(n):
    if sum_of_divisors(n) > n:
        return True
    else:
        return False


def generate_abundace(fpath, fname='abundants.txt'):
    """
    Generate relevant abundant numbers, write
    them to a file.
    TODO: Remove this dependence.
    """
    abundants = []
    for i in range(1, 28124):
        if is_abundant(i) > i:
            abundants.append(i)

    with open(fpath + fname, 'w') as f:
        f.write("%s\n" % '\n'.join(abundants))


def load_abundants(fpath, fname='abundants.txt'):
    with open(fpath + fname) as f:
        abundants = map(int, f.read().splitlines())
    return abundants


@clock
def main():
    # Perform some cheating io
    abundants = load_abundants('/Users/rileyde/Documents/projects/euler/data/')
    num_abundants = len(abundants)
    
    answer = 0
    limit = 28124
    is_abundant = [False] * limit 
    
    for i in range(num_abundants):
        for j in range(i, num_abundants):
            abundant_sum = abundants[i] + abundants[j]
            if (abundant_sum) <= limit:
                is_abundant[abundant_sum - 1] = True
            else:
                break
    
    for i in range(limit):
        if not is_abundant[i]:
            answer += i + 1
    
    return answer 


if __name__ == '__main__':
    main()

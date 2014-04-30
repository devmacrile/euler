#Devin Riley
#Project Euler
#Problem 16
#12/30/2013

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import time

start = time.time()

def sum_of_digits(n):
    #returns sum of digits of an integer n
    result = 0
    tracker = n
    while(tracker > 0):
        result += tracker % 10
        tracker = (tracker - tracker%10)/10
    return result


big_int = pow(2,1000)
result = sum_of_digits(big_int)
elapsed = (time.time() - start)

print "Sum of digits of 2^1000 is %s, and it took %s to find this." %(result, elapsed)

#Sum of digits of 2^1000 is 1366, and it took 0.00082802772522 to find this.
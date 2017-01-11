"""
The Fibonacci sequence is defined by the recurrence relation:

Fn =  Fn - 1 + Fn - 2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 88
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

from eutil import clock


@clock
def main():
    fibnum = 1
    a = 0
    b = 1
    while(len(str(b)) < 1000):
        a, b = b, a + b
        fibnum += 1
    return fibnum        

#The answer is 4782, which was found in 0.0495409965515 seconds
    
if __name__ == '__main__':
    main()


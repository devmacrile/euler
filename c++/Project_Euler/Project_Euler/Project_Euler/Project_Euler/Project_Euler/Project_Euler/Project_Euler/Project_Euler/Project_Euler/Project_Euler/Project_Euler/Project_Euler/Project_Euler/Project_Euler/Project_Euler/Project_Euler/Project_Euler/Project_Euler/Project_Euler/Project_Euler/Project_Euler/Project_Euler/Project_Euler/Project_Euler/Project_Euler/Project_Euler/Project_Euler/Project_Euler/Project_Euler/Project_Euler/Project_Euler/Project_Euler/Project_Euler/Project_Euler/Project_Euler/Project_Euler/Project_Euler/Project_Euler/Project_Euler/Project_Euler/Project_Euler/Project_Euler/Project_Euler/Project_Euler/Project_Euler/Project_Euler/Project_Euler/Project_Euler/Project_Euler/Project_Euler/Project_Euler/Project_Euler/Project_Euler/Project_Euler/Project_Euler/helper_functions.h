//
//  helper_functions.h
//  Project_Euler
//
//  Created by Devin Riley on 6/9/13.
//  Copyright (c) 2013 Devin Riley. All rights reserved.
//

#ifndef __Project_Euler__helper_functions__
#define __Project_Euler__helper_functions__

#include <iostream>


int fib(int n);
//Requires: n >=0
//Effects: calculates the nth fibonacci number
int factorial(int n);
// returns n!
bool isPrime(int n);
// returns trure if n is prime, false otherwise
bool checkPrime(long n);
// returns true if n is prime, false otherwise
int sieveOfEratos(int n);
// returns sum of all primes less than n


int lcm(int a, int b);
// calculates least common multiple of a, b
int gcd(int a, int b);
// calculates greatest commond divisor of a, b

int sumOfSquares(int a, int b);
// calculates sum of squares from integer a to b
// requires that b >= a!
// i.e. a^2 + (a+1)^2 + .... + (b-1)^2 + b^2
int squareOfSums(int a, int b);
// calculates square of sum of integers from a to b
// requires again that b>=a
// i.e. (a + (a+1) + (a+2) + ..... + (b-1) + b)^2



#endif /* defined(__Project_Euler__helper_functions__) */

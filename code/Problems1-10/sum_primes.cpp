//
//  sum_primes.cpp
//  Project_Euler
//
//
/*
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 
 Find the sum of all the primes below two million.
 */

#include "sum_primes.h"
#include "helper_functions.h"
#include <iostream>
using namespace std;

long sumPrimes(long n){
    // Pretty fast for 2000000, only have to check prime up to sqrt(n)
    // Likely a better way though (than trial division); sieve?
    long sum = 0;
    for(long i=2; i<=n; ++i){
        if(checkPrime(i)){
            sum += i;
        }
    }
    return sum;
}




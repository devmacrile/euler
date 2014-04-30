//
//  bigPrime.cpp
//  Project_Euler
//
//
//
/*
 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 
 What is the 10 001st prime number?
 */

// naive idea is obviously just to while loop through the integers, checking for prime
// and keeping track of how many primes there have been

#include "bigPrime.h"
#include "helper_functions.h"
#include <iostream>
using namespace std;

int bigPrime(int n){
    int tracker = 0;// keep track of how many primes we have encountered
    int iter = 1;//start on first prime #, will end up being the result
    while(tracker < n){
        iter += 1;
        if(isPrime(iter)){
            tracker += 1;
        }
    }
    
    return iter;
}
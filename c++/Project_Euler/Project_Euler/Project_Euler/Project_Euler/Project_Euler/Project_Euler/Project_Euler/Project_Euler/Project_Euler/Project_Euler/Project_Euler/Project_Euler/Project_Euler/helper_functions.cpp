//
//  helper_functions.cpp
//  Project_Euler
//
// Collection of functions that I felt may be useful across problems, after requiring them for
// the solution of at least one problem
//

#include "helper_functions.h"
#include <iostream>
#include <cmath>
using namespace std;

// calculate nth fibonacci number
int fib(int n){
    if(n==0 || n==1)
        return n;
    else{
        return fib(n-1) + fib(n-2);
    }
    
    
}

// integer prime or not
//very inefficient! is there a better way?
bool isPrime(int n){
    if(n==1 || n == 2)
        return true;
    for(int j=2; j<=sqrt(n); ++j){
        if(n%j == 0)
            return false;
    }
    return true;
}

//check prime for large numbers (bigger than int)
bool checkPrime(long n){
    if(n==1 || n == 2)
        return true;
    for(long j=2; j<=sqrt(n); ++j){
        if(n%j == 0)
            return false;
    }
    return true;
}


// calculates factorial of n recursively
int factorial(int n){
    if(n==1)
        return 1;
    else{
        return n*factorial(n-1);
    }
}

// greatest common divisor of two integers
int gcd(int a, int b){
    if(a == b)
        return a;
    else if(a>b){
        return gcd(b, a-b);
    }
    else{
        return gcd(a, b-a);
    }
}

// least common multiple of two integers
int lcm(int a, int b){
    return (a*b)/gcd(a,b);
}

// sum of squares of integers on [a,b]
int sumOfSquares(int a, int b){
    int ss = 0;
    for(int i=a; i<b+1; ++i){
        ss += i*i;
    }
    
    return ss;
}

// squareOfSums of integers on [a,b]
int squareOfSums(int a, int b){
    int sum = 0, result = 0;
    sum = (b+1)*b/2 - (a)*(a-1)/2;
    result = sum*sum;
    return result;
}






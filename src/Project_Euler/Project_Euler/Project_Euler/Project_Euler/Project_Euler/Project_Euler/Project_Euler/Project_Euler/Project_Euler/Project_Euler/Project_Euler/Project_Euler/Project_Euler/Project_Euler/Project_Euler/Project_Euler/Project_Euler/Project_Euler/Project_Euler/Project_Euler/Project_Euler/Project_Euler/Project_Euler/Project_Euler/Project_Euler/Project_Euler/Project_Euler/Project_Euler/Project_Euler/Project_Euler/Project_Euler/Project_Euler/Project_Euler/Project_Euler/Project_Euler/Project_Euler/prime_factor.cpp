//
//  prime_factor.cpp
//  Project_Euler
//
//  Find largest prime factor of given number
//

#include "prime_factor.h"
#include "helper_functions.h"
#include <cmath>
#include <iostream>
using namespace std;

void largestPrimeFactor(long long bigNumber){
    int largest = 1;
    cout << largest << endl;
    if(bigNumber%2 == 0)
        cout << "even" << endl;
        largest+=1;
    for(int i=3; i<bigNumber/2; i=i+2){
        if(bigNumber%i == 0 && isPrime(i)){
            cout << i << endl;
            largest = i;
        }
    }
    
    cout << largest;
    
}












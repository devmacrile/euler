//
//  main.cpp
//  Project_Euler
//
//  
//  


#include <iostream>
#include <fstream>
//#include "even_fibonacci.h" // problem 2
//#include "prime_factor.h" //problem 3
//#include "largest_palindrome.h" //problem 4
//#include "smallest_multiple.h" // problem 5
//#include "ss_diff.h" // problem 6
//#include "bigPrime.h" // problem 7
//#include "largestProduct.h" // Problem 8
//#include "pythagorean_triplet.h" // problem 9
//#include "sum_primes.h" // Problem 10
#include "gridProduct.h" // Problem 11
#include "helper_functions.h"
#include <time.h>
using namespace std;

int main(int argc, const char * argv[])
{
    //evenFibMain(4000000); // Problem 2: sum of even fibonacci #s less that 4000000
    //largestPrimeFactor(600851475143); // Problem 3: Largest prime factor of #
    //largestPalindromeProd(); // Problem 4: Largest palindrome product of 3 digit numbers
    //smallestMultiple(20); // Problem 5: Smallest number of which all of 1-20 are factors
    //cout << ssDiff(0,100); // problem 6 : sqSum - sumSq for range of ints
    //cout << bigPrime(10001) << endl; // Problem 7
    //largestProduct(); //8
    //cout << "result: " << pythagoreanTriplet() << endl; // Problem 9 three numbers such that a^2+b^2 = c^2 where a+b+c=1000
    //cout << sumPrimes(2000000); //Problem 10
    //int myGrid[20][20]; // Problem 11
    //readGrid(myGrid);// Finished in python
    //Problem 12 done in python
    
    clock_t t;
    t = clock();
    int j = 0;
    for(int i=0; i<10000000; ++i){
        j = i + 1;
    }
    
    t = clock() - t;
    cout << "seconds: " << t << endl;
    
    
}






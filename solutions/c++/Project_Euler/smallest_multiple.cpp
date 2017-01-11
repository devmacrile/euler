//
//  smallest_multiple.cpp
//  Project_Euler
//
//
/*
 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 
 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */




#include <iostream>
#include "smallest_multiple.h"
#include "helper_functions.h"
using namespace std;

void smallestMultiple(int n){
    int range [n];
    for(int i=0; i<n; ++i){ //put numbers 1..n in an array
        range[i] = i + 1;
    }
    
    //remember the awesome fact that there is an isomorphism between integers
    //and prime factorizations (fundamental theorem of arithmetic)
    int result = 1;
    for(int i=0; i<n; ++i){//idea is to get prime factorizations of each number 1..n
        if(range[i] > 1){// but removing duplicates in the process...
            int factor = range[i];//
            result *= factor;
            for(int j=i; j<n; j=j+factor){
                if(range[j] >= range[i]){//should always be true, but for safety
                    range[j] /= factor;//remove from other factorizations of which factor
                    // plays a part (i.e. 2 is 2*1, 4 is 2*2*1, but don't need 3 twos)
                }
            }
        }
    }
        
    cout << "And the result is... " << result << endl;
    
}

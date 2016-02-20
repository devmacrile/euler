//
//  pythagorean_triplet.cpp
//  Project_Euler
//
//
/*
 A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
 
 a2 + b2 = c2
 For example, 32 + 42 = 9 + 16 = 25 = 52.
 
 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.
 */

#include "pythagorean_triplet.h"
#include "helper_functions.h"
using namespace std;

int pythagoreanTriplet(){
    for(int i=1; i<500; ++i){
        for(int j = 1; j<500; ++j){
            int ss = i*i + j*j;
            int c = 1000 - (i+j);
            cout << i << " " << j << " " << c << " " << ss << " " << c*c << endl;
            if((ss == c*c) && (i+j+c==1000)){
                cout << "a,b,c = " << i << "," << j << "," << c << endl;
                return i*j*c;
            }
            
        }
    }
    return -1;//couldn't find the triplet
}



int sqrt(int b){
    int root = 1;
    while(root*root <= b){
        if(root*root == b){
            return root;
        }
        root += 1;
    }
    return -1;
}


bool hasSqRoot(int b){
    int counter = 0;
    while(counter*counter <= b){
        if(counter*counter == b){
            return true;
        }
        counter += 1;
    }
    return false;
    
}


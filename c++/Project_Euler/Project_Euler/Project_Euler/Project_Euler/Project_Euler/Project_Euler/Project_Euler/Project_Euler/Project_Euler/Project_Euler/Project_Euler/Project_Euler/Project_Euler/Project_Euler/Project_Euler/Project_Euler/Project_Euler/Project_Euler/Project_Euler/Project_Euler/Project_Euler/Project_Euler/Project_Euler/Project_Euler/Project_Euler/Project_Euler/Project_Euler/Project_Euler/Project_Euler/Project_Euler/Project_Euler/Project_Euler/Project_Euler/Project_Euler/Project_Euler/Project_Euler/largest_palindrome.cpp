//
//  largest_palindrome.cpp
//  Project_Euler
//
//
/*
 A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
 
 Find the largest palindrome made from the product of two 3-digit numbers.
 */



#include "largest_palindrome.h"
#include "helper_functions.h"
#include <iostream>
using namespace std;


void largestPalindromeProd(){
    int outside = 9, middle = 0, inside = 0;
    int largest = 0;
    for(int i = 0; i<10; ++i){
        middle = i;
        for(int j = 0; j<10; ++j){
            inside = j;
            int my_pal = outside + 10*middle + 100*inside + 1000*inside + 10000*middle + 100000*outside;
            //cout << my_pal << " " << endl;
            if(my_pal > largest && has_3digit_product(my_pal)){
                largest = my_pal;
            }
        }
    }
    cout << "And the winner is... " << largest << endl;
}


bool has_3digit_product(int pal){
    for(int i=100; i<1000; ++i){
        if(pal%i == 0 && pal/i < 1000 && pal/i > 100){
            return true;
        }
    }
    return false;
}

    

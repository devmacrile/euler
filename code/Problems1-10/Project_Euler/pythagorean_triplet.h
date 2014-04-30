//
//  pythagorean_triplet.h
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

#ifndef __Project_Euler__pythagorean_triplet__
#define __Project_Euler__pythagorean_triplet__

#include <iostream>
using namespace std;

int pythagoreanTriplet();
//returns pythagorean triplet for 1000
int sqrt(int b);
//returns the integer square root of b; if none, returns -1
bool hasSqRoot(int b);
//returns true if b has integer square root
#endif /* defined(__Project_Euler__pythagorean_triplet__) */

//
//  even_fibonacci.cpp
//  Project_Euler
//
//

#include "even_fibonacci.h"
#include "helper_functions.h"
using namespace std;


void evenFibMain(int limit){
    // sloppy/inefficient as fib recursively calls every time (same call being made over and over)
    int evenFib_sum = 0;
    int counter = 0, cur_fib = 0;
    while(cur_fib < limit){
        cur_fib = fib(counter);
        if(cur_fib%2 == 0){
            evenFib_sum += cur_fib;
        }
        counter += 1;
    }
    
    std::cout << evenFib_sum << endl;
}




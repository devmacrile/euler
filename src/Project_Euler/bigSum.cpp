//
//  bigSum.cpp
//  Project_Euler
//
//  Created by Devin Riley on 6/11/13.
//  Copyright (c) 2013 Devin Riley. All rights reserved.
//

#include "bigSum.h"
#include "helper_functions.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int bigSum(){
    ifstream filestream();
    string line;
    while(filestream.good()){
        getline(filestream, line);
        int fiftydigits = str_to_int(line);
        
    }
    
    
    
    
}



void readNumbers(int grid[20][20){
    ifstream filestream("/Users/rileyde/Documents/Project_Euler/Project_Euler/number_grid.txt");
    string line;
    while(filestream.good()){//while still rows to be read
        int row = 0;
        getline(filestream, line);//store line of numbers in string
        string tokens[20];
        tokenize(line, tokens);
        for(int i=0; i<20; ++i){
            grid[row][i] = str_to_int(tokens[i]);
        }
        row +=1; //increment row index
    }
    printGrid(grid);
}
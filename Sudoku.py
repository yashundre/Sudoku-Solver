# -*- coding: utf-8 -*-
import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def possible(row,column,number):
    global grid
    #to check in row
    for i in range(0,9):
        if grid[row][i] == number:
            return False
     
    #to check in column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #to check in box
    xo = (column//3)*3 #for initializing search at start row of the box
    yo = (row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[yo+i][xo+j] == number:
                return False
    return True

def solve():
    global grid
    
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column]==0:
                for number in range(1,10):
                    if possible(row,column,number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))
    input("More Possible solutions")
solve()
                
            
    
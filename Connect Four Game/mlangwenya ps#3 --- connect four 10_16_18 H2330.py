# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:15:49 2018

@author: mdudu
"""

#-------------------------------------------Functions-------------------------------------------------------
def game_input(player):
    play = int(input("%s's Turn: Please make column selection (0-6)!" % str(player)))
    while play < 0 or play > 6:
        play = int(input("%s's Turn: Please make column selection (0-6)!" % str(player)))
    return play
        
def make_grid(grid, grid_symbol, move):
    nrows = [0,1,2,3,4,5]
    for s in nrows:
        if grid[s][move] == 0:
            row_number = s
    grid[row_number][move] = grid_symbol
    return grid

def is_winner(grid, grid_symbol):
    nrows = [0,1,2,3,4,5]
    #horizontal check
    for k in range(4):
        for l in range(0, len(nrows)):
            if grid[l][k] == grid_symbol and grid[l][k+1] == grid_symbol and grid[l][k+2] == grid_symbol and grid[l][k+3] == grid_symbol:
                return True 
    #vertical check
    for m in range(7):
        for n in range(3):
            if grid[n][m] == grid_symbol and grid[n+1][m] == grid_symbol and grid[n+2][m] == grid_symbol and grid[n+3][m] == grid_symbol:
                return True
    #positive slope check
    for r in range(4):
        for p in range(3,6):
            if grid[p][r] == grid_symbol and grid[p-1][r+1] == grid_symbol and grid[p-2][r+2] == grid_symbol and grid[p-3][r+3] == grid_symbol:
                return True
    #negative slope check
    for r in reversed(range(3,7)):
        for p in range(3,6):
            if grid[p][r] == grid_symbol and grid[p-1][r-1] == grid_symbol and grid[p-2][r-2] == grid_symbol and grid[p-3][r-3] == grid_symbol:
                return True
            
def computer_move(grid):
    nrows = [0,1,2,3,4,5]
    grid_symbol = 5
    flag = True
    #horizontal check #3
    for k in range(4):
        for l in range(0, len(nrows)):
            if l == 5:
                if grid[l][k] == 5 and grid[l][k+1] == 5 and grid[l][k+2] == 5 and grid[l][k+3] == 0.0 and flag:
                    row_number = k+3; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 10 and grid[l][k+1] == 10 and grid[l][k+2] == 10 and grid[l][k+3] == 0.0 and flag:
                    row_number = k+3; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 0.0 and grid[l][k+1] == 10 and grid[l][k+2] == 10 and grid[l][k+3] == 10 and flag:
                    row_number = k; grid[l][row_number] = grid_symbol; flag = False
            else: 
                if grid[l][k] == 5 and grid[l][k+1] == 5 and grid[l][k+2] == 5 and grid[l][k+3] == 0.0 and grid[l+1][k+3] !=0.0 and flag:
                    row_number = k+3; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 10 and grid[l][k+1] == 10 and grid[l][k+2] == 10 and grid[l][k+3] == 0.0 and grid[l+1][k+3] !=0.0 and flag:
                    row_number = k+3; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 0.0 and grid[l][k+1] == 10 and grid[l][k+2] == 10 and grid[l][k+3] == 10 and grid[l+1][k] !=0.0 and flag:
                    row_number = k; grid[l][row_number] = grid_symbol; flag = False
    #vertical check #3
    for m in range(7):
        for n in range(3):
            if grid[n][m] == 0.0 and grid[n+1][m] == 5 and grid[n+2][m] == 5 and grid[n+3][m] == 5 and flag:
                row_number = n; grid[row_number][m] = grid_symbol; flag = False
            if grid[n][m] == 0.0 and grid[n+1][m] == 10 and grid[n+2][m] == 10 and grid[n+3][m] == 10 and flag:
                row_number = n; grid[row_number][m] = grid_symbol; flag = False           
    #positive slope check #3
    for r in range(4):
        for p in range(3,6):
            if grid[p][r] == 5 and grid[p-1][r+1] == 5 and grid[p-2][r+2] == 5 and grid[p-3][r+3] == 0.0 and grid[p-2][r+3] != 0.0 and flag:
                grid[p-3][r+3] = grid_symbol; flag = False
            if grid[p][r] == 0.0 and grid[p-1][r+1] == 5 and grid[p-2][r+2] == 5 and grid[p-2][r+3] == 5 and flag:
                grid[p][r] = grid_symbol; flag = False
            if grid[p][r] == 10 and grid[p-1][r+1] == 10 and grid[p-2][r+2] == 10 and grid[p-3][r+3] == 0.0 and grid[p-2][r+3] != 0.0 and flag:
                grid[p-3][r+3] = grid_symbol; flag = False 
            if grid[p][r] == 0.0 and grid[p-1][r+1] == 10 and grid[p-2][r+2] == 10 and grid[p-3][r+3] == 10 and flag:
                grid[p][r] = grid_symbol; flag = False
    #negative slope check #3
    for r in reversed(range(3,7)):
        for p in range(3,6):
            if grid[p][r] == 5 and grid[p-1][r-1] == 5 and grid[p-2][r-2] == 5 and grid[p-2][r-3] != 0.0 and flag :
                grid[p-3][r-3] = grid_symbol; flag = False  
            if grid[p][r] == 10 and grid[p-1][r-1] == 10 and grid[p-2][r-2] == 10 and grid[p-3][r-3] == 0.0 and grid[p-2][r-3] != 0.0 and flag :
                grid[p-3][r-3] = grid_symbol; flag = False
            if grid[p][r] == 0.0 and grid[p-1][r-1] == 10 and grid[p-2][r-2] == 10 and grid[p-3][r-3] == 10 and flag :
                grid[p][r] = grid_symbol; flag = False  
                
    #positive slope check #2
    for r in range(4):
        for p in range(3,6):
            if grid[p][r] == 10 and grid[p-1][r+1] == 10 and grid[p-2][r+2] == 0.0 and grid[p-2][r+3] != 0.0 and flag:
                grid[p-2][r+2] = grid_symbol; flag = False 

    #negative slope check #2
    for r in reversed(range(3,7)):
        for p in range(3,6):
            if grid[p][r] == 10 and grid[p-1][r-1] == 10 and grid[p-2][r-2] == 0.0 and grid[p-2][r-3] != 0.0 and flag :
                grid[p-2][r-2] = grid_symbol; flag = False  
    
                         
    #horizontal check #2
    for k in range(4):
        for l in range(0, len(nrows)):
            if l == 5:
                if grid[l][k] == 10 and grid[l][k+1] == 10 and grid[l][k+2] == 0.0 and grid[l][k+3] == 0.0 and flag:
                    row_number = k+2; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 0.0 and grid[l][k+1] == 0.0 and grid[l][k+2] == 10 and grid[l][k+3] == 10 and flag:
                    row_number = k+1; grid[l][row_number] = grid_symbol; flag = False
            else:
                if grid[l][k] == 10 and grid[l][k+1] == 10 and grid[l][k+2] == 0.0 and grid[l][k+3] == 0.0 and grid[l+1][k+3] != 0.0 and flag:
                    row_number = k+2; grid[l][row_number] = grid_symbol; flag = False
                if grid[l][k] == 0.0 and grid[l][k+1] == 0.0 and grid[l][k+2] == 10 and grid[l][k+3] == 10 and grid[l+1][k+3] == 0.0 and flag:
                    row_number = k+1; grid[l][row_number] = grid_symbol; flag = False
    #vertical check #2 
    for m in range(7):
        for n in range(3): 
            if grid[n][m] == 0.0 and grid[n+1][m] == 0.0 and grid[n+2][m] == 10 and grid[n+3][m] == 10 and flag:
                row_number = n+1; grid[row_number][m] = grid_symbol; flag = False
                
    #horizontal check #1
    for k in range(4):
        for l in range(0, len(nrows)):
            if grid[l][k] == 10 and grid[l][k+1] == 0.0 and grid[l][k+2] == 0.0 and grid[l][k+3] == 0.0 and l == 5 and flag:
                row_number = k+1; grid[l][row_number] = grid_symbol; flag = False
            if grid[l][k] == 0.0 and grid[l][k+1] == 0.0 and grid[l][k+2] == 0.0 and grid[l][k+3] == 10 and l == 5 and flag:
                row_number = k+2; grid[l][row_number] = grid_symbol; flag = False
    #vertical check #1
    for m in range(7):
        for n in range(3): 
            if grid[n][m] == 0.0 and grid[n+1][m] == 0.0 and grid[n+2][m] == 10 and grid[n+3][m] == 10 and flag:
                row_number = n+1; grid[row_number][m] = grid_symbol; flag = False
            if grid[n][m] == 0.0 and grid[n+1][m] == 0.0 and grid[n+2][m] == 0.0 and grid[n+3][m] == 10 and flag :
                row_number = n+2; grid[row_number][m] = grid_symbol; flag = False
    #random
    for k in range(0, 4):
        for l in range(0, 5):
            if l == 5 and grid[5][k] == 0.0 and flag:
                grid[l][k] = grid_symbol; flag = False
            if l < 3 and grid[l+1][k] != 0.0 and flag: 
                grid[l][k] = grid_symbol; flag = False 
                      
#######################################################################################
import numpy as np
grid = np.zeros((6,7))
count = 0  
flag = True
print(grid)

while flag == True:
    if count == 0:
        player = "Human"; grid_symbol = 10
        move = game_input(player)
        make_grid(grid, grid_symbol, move); print("\nHuman plays as 10\n", grid)
        if is_winner(grid, grid_symbol) == True:
            print("\nCongrats, %s wins the game!\n" % str(player))
            break          
        count += 1 
        count = count % 2 
    else:
        player = "Computer"; grid_symbol = 5
        print("\n%s's Turn: Please make column selection (0-6)!" % str(player))
        computer_move(grid); print("\nComputer plays as 5\n", grid)
        if is_winner(grid, grid_symbol) == True:
            print("\nOops, %s wins the game!\n" % str(player))
            break 
        count += 1 
        count = count % 2 

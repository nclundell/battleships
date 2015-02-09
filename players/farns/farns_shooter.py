#@author Nathan Lundell
#@date January 2015
#@player farnsworth
#
#Shooter for @player
#
#Based on Farnsworth Player by Nate Kohl
#Link: http://natekohl.net/files/FarnsworthOpponent.cs

import sys
import random

sys.path.append("../../")

from b_globals import *
from b_functions import *

class FarnsworthShooter:
    def __init__(self):
        #Basic player variables
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[0]*board_size for i in range(board_size)]
        self.row = 0
        self.col = 0
        #Locations to explore
        self.must_explore = []
        #Amount of space around each location
        self.left = [[0]*board_size for i in range(board_size)]
        self.right = [[0]*board_size for i in range(board_size)]
        self.down = [[0]*board_size for i in range(board_size)]
        self.up = [[0]*board_size for i in range(board_size)]
        #How much space each location has
        self.space = [[0]*board_size for i in range(board_size)]
        #How many possible hits each location has
        self.hits = [[0]*board_size for i in range(board_size)]
        #Game Variables
        self.kills = []
        self.wins = 0
        
    def reset(self):
        #Basic player variables
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.row = 0
        self.col = 0
        #Locations to explore
        self.must_explore = []
        #Amount of space around each location
        self.left = [[0]*board_size for i in range(board_size)]
        self.right = [[0]*board_size for i in range(board_size)]
        self.down = [[0]*board_size for i in range(board_size)]
        self.up = [[0]*board_size for i in range(board_size)]
        self.reset_hits()
        self.space = [[0]*board_size for i in range(board_size)]
        #Game Variables
        self.kills = []
    
    def reset_hits(self):
        for i in range(board_size):
            for j in range(board_size):
                if(self.shot_board[i][j] == HIT or self.shot_board[i][j] == KILL):
                    self.hits[i][j] = 1
                else:
                    self.hits[i][j] = 0
    
    def make_shot(self, shot_count):
        if(len(self.must_explore) > 0 ):
            #print(1)
            self.row, self.col = self.must_explore.pop(0)
        if(self.get_hit()):
            #print(2)
            self.row, self.col = self.must_explore.pop(0)
        if(self.get_space()):
            #print(3)
            self.row, self.col = self.must_explore.pop(0)
        return [self.row, self.col]
    
    def mark_shot(self, shot, result):
        self.shot_board[shot[0]][shot[1]] = result
     
    #Search for remaining hits, add to must_explore
    def get_hit(self):
        count = 0
        
        for i in range(board_size):
            for j in range(board_size):
                if(self.shot_board[i][j] == HIT):
                    for ship in ships:
                        if(ship not in self.kills):
                            #Check Horizontal
                            left = j
                            right = j
                            while left > 0 and left > (j-(ship-1)) and self.shot_board[i][left] != KILL:
                                left -= 1
                            while right < board_size and right < (j+(ship-1)) and self.shot_board[i][right] != KILL:
                                right += 1
                            
                            #Check Vertical
                            up = i
                            down = i
                            while up > 0 and up > (i-(ship-1)) and self.shot_board[up][j] != KILL:
                                up -= 1
                            while down < board_size and down <(i+(ship-1)) and self.shot_board[down][j] != KILL:
                                down += 1
                                
                            #Get number of possible ships on area
                            if(right - left + 1 >= ship):
                                for s in range(left, right):
                                    if(self.shot_board[i][s] == WATER):
                                        self.hits[i][s] += 1
                                        count += 1
                            if(down - up + 1 >= ship):
                                for s in range(up, down):
                                    if(self.shot_board[s][j] == WATER):
                                        self.hits[s][j] += 1
                                        count += 1
        if(count > 0):
            self.get_best(self.hits)
            return True
        return False
    
    #Explore if no hits on board, add to must_explore
    def get_space(self):
        for i in range(board_size):
            for j in range(board_size):
                self.compute_adjacent_space(i, j)
                for ship in ships:
                    if(ship not in self.kills):
                        #Check Horizontal
                        if(self.left[i][j] < ship-1):
                            left_pos = self.left[i][j]
                        else:
                            left_pos = ship-1
                        if(self.right[i][j] < ship-1):
                            right_pos = self.right[i][j]
                        else:
                            right_pos = ship-1
                        
                        #Check Vertical
                        if(self.up[i][j] < ship-1):
                            up_pos = self.up[i][j]
                        else:
                            up_pos = ship-1
                        if(self.down[i][j] < ship-1):
                            down_pos = self.down[i][j]
                        else:
                            down_pos = ship-1
                        
                self.space[i][j] = abs(left_pos + right_pos + up_pos + down_pos)
        return self.get_best(self.space)  
    
    def compute_adjacent_space(self, row, col):
        if(self.shot_board[row][col] != WATER):
            self.left[row][col] = 0
            self.right[row][col] = 0
            self.up[row][col] = 0
            self.down[row][col] = 0
        else:
            #Left
            if(col == 0 or self.shot_board[row][col-1] != WATER):
                self.left[row][col] = 0
            else:
                self.left[row][col] = self.left[row][col-1] + 1
            #Right
            if(col == 0 or self.shot_board[row][col-1] == 0):
                counter = 0
                for i in range(col+1, board_size):
                    if(self.shot_board[row][i] != WATER):
                        break
                    counter += 1
                self.right[row][col] = counter
            else:
                self.right[row][col] = self.right[row][col-1] - 1
            #Up
            if(row == 0 or self.shot_board[row-1][col] != WATER):
                self.up[row][col] = 0
            else:
                self.up[row][col] = self.up[row-1][col] + 1
            #Down
            if(row == 0 or self.down[row-1][col] == 0):
                counter = 0
                for i in range(row+1, board_size):
                    if(self.shot_board[i][col] != WATER):
                        break
                    counter += 1
                self.down[row][col] = counter
            else:
                self.down[row][col] = self.down[row-1][col] - 1
    
    #Get largest element, and randomly choose if multiple matches found
    def get_best(self, arr):
        largest = 0
        count = 0
        for i in range(board_size):
            for j in range(board_size):
                if(arr[i][j] > largest and self.shot_board[i][j] == WATER):
                    largest = arr[i][j]
                    count += 1
                elif(self.hits[i][j] == largest and self.shot_board[i][j] == WATER):
                    count += 1
        if(count > 0):
            while True:
                for i in range(board_size):
                    for j in range(board_size):
                        if(arr[i][j] == largest):
                            if(random.random() < (1.0/count)):
                                self.must_explore.append([i, j])
                                return
        else:
            for i in range(board_size):
                for j in range(board_size):
                    if(self.shot_board[i][j] == WATER):
                        count += 1
            print("All locatons shot at!",count)
            print_board(self.hits)
            print_board(self.space)
            sys.exit(0)
                
                
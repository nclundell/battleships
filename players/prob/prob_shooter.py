#@author Nathan Lundell
#@date January 2015
#@player prob
#
#Target and Shoot for @player

import sys

sys.path.append("../../")

from b_globals import *
from b_functions import *

class prob_shooter:
    def __init__(self):
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.prob_board = [[0]*board_size for i in range(board_size)]
        self.last_row = 0
        self.last_col = 0
        self.kills = 0
        self.wins = 0
        
    def reset(self):
        self.reweigh_board() #Reweigh instead of resetting to bring successful shots over to next game
        self.shot_board = [[WATER]*board_size for i in range(board_size)]
        self.kills = 0
        self.last_row = 0
        self.last_col = 0
        
    def make_shot(self, shot_count):
        if(self.shot_board[self.last_row][self.last_col] == HIT):
            self.finish_ship()
        elif(self.damaged_ship_exists()):
            self.finish_ship()
        else:
            self.reweigh_board()
            self.probe_for_best_shot()
        return [self.last_row, self.last_col]
        
    def mark_shot(self, shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        
    def finish_ship(self):
        #Search Up
        r = self.last_row-1
        c = self.last_col
        while r >= 0:
            if(self.shot_board[r][c] == WATER):
                self.last_row = r
                return
            if(self.shot_board[r][c] == KILL or self.shot_board[r][c] == MISS):
                break
            r -= 1

        #Search Left
        r = self.last_row
        c = self.last_col-1
        while c >= 0:
            if(self.shot_board[r][c] == WATER):
                self.last_col = c
                return
            if(self.shot_board[r][c] == KILL or self.shot_board[r][c] == MISS):
                break
            c -= 1
        
        #Search Down
        r = self.last_row+1
        c = self.last_col
        while r < board_size:
            if(self.shot_board[r][c] == WATER):
                self.last_row = r
                return
            if(self.shot_board[r][c] == KILL or self.shot_board[r][c] == MISS):
                break
            r += 1

        #Search Right
        r = self.last_row
        c = self.last_col+1
        while c < board_size:
            if(self.shot_board[r][c] == WATER):
                self.last_col = c
                return
            if(self.shot_board[r][c] == KILL or self.shot_board[r][c] == MISS):
                break
            c += 1
    
    def damaged_ship_exists(self):
        for i in range(board_size):
            for j in range(board_size):
                if(self.shot_board[i][j] == HIT):
                    self.last_row = i
                    self.last_col = j
                    return True
        return False
        
    def reweigh_board(self):
        for i in range(board_size):
            for j in range(board_size):
                self.prob_board[i][j] = self.new_weight(i, j)
                
    def new_weight(self, row, col):
        weight = 0.0
        
        #for i in range((ship_max_length - ship_min_length)+1):
        for i in range(ship_max_length - ship_min_length):
            weight += self.get_vertical_weight(row, col, i)
            weight += self.get_horizontal_weight(row, col, i)
        return float(weight)
            
    def get_vertical_weight(self, row, col, length):
        weight = 0.0
        high = row
        low = row
        while(low >= 0 and row-low < length):
            if(self.shot_board[low][col] == KILL or self.shot_board[low][col] == MISS):
                break
            low -= 1
        while(high<board_size and high-row < length):
            if(self.shot_board[high][col] == KILL or self.shot_board[high][col] == MISS):
                break
            high += 1
        if(high-low >= length):
            weight += high-low-length
        return weight
    
    def get_horizontal_weight(self, row, col, length):
        weight = 0.0
        high = col
        low = col
        while(low >= 0 and col-low < length):
            if(self.shot_board[row][low] == KILL or self.shot_board[row][low] == MISS):
                break
            low -= 1
        while(high < board_size and high-col < length):
            if(self.shot_board[row][high] == KILL or self.shot_board[row][high] == MISS):
                break
            high += 1
        if(high-low >= length):
            weight += high-low-length
        return weight
    
    def probe_for_best_shot(self):
        max_weight = -1
        for i in range(board_size):
            for j in range(board_size):
                weight = self.prob_board[i][j]
                if(weight > max_weight):
                    max_weight = weight
                    self.last_row = i
                    self.last_col = j
    
    def read_initial_probs(self):
        board = []
        probs = open('players/prob/initial.dat', 'r')
        for line in probs:
            board.append(line.strip('\r\n').split(','))
        #Convert Each Item to Float
        for i in range(board_size):
            for j in range(board_size):
                board[i][j] = float(board[i][j])            
        return board[:][:]
        
    

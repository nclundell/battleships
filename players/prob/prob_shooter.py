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
        self.prob_board = self.read_initial_probs()
        self.last_row = 0
        self.last_col = 0
        self.wins = 0 #Total Wins in Full Match
        
    def make_shot(self, shot_count):
        if(self.shot_board[self.last_row][self.last_col] == HIT):
            finish_ship()
        elif(self.damaged_ship_exists()):
            self.finish_ship()
        else:
            self.probe_for_best_shot()
        return [self.last_row, self.last_col]
        
    def mark_shot(self, shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        #print "Probability Board: \n"
        #print_board(self.prob_board)
        self.reweigh_board() #Reweigh prob board after every turn
        
    def reset(self):
        self.prob_board = self.reweighBoard() #Reweigh before resetting shot board to bring successful shots over to next game
        self.shot_board = [[WATER]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0
        
    def finish_ship(self):
        #Search Up
        if(self.probe_for_kill(-1, 0, ship_max_length)):
            return
        elif (self.shot_board[self.last_row-1][self.last_col] == HIT):
            if(self.probe_for_kill(1, 0, ship_max_length-1)):
                return
        #Search Left and Right
        if(self.probe_for_kill(0, 1, ship_max_length)):
            return
        elif(self.shot_board[self.last_row][self.last_col+1] == HIT):
            if(self.probe_for_kill(0, -1, ship_max_length-1)):
                return
        #Seach Down
        if(self.probe_for_kill(1, 0, ship_max_length)):
            return
        if(self.probe_for_kill(0, -1, ship_max_length)):
            return
        else:
            self.probe_for_best_shot()
            return
    def probe_for_kill(self, row_jump, col_jump, jump_range):
        if(jump_range <= 0):
            return False
        if(self.shot_board[self.last_row][self.last_col] == MISS or self.shot_board[self.last_row][self.last_col] == KILL):
            return False
        elif(self.shot_board[self.last_row][self.last_col] == WATER):
            return True
        elif(self.probe_for_kill(self.last_row+row_jump, self.last_col+col_jump, jump_range-1)):
            return True
        return False
    
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
                self.prob_board = self.new_weight(i, j)
                
    def new_weight(self, row, col):
        weight = 0.0
        for i in range(ship_max_length - ship_min_length):
            weight += self.get_vertical_weight(row, col, i)
            weight += self.get_horizontal_weight(row, col, i)
        return float(weight)
            
    def get_vertical_weight(self, row, col, length):
        weight = 0
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
        weight = 0
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
        
    
    
    
    
    
    
    
    
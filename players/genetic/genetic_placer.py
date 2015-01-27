#@author Nathan Lundell
#@date January 2015
#@player genetic
#
#Ship Placer for @player

import sys

sys.path.append("../../")

from b_globals import *
from b_functions import *

class genetic_placer:
    def __init__(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.prob_board = self.get_initial_probs()
        self.last_row = 0
        self.last_col = 0

    def place_ship(self, length, marker):
        return 0
    
    def mark_shot(self, shot, result):
        self.ship_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.ship_board = [["W"]*board_size for i in range(board_size)]
        
    def get_initial_probs(self):
        board = []
        probs = open('players/genetic/data/initial_placement_data.dat', 'r')
        for line in probs:
            board.append(line.strip('\r\n').split(','))
        #Convert Each Item to Float
        for i in range(board_size):
            for j in range(board_size):
                board[i][j] = float(board[i][j])            
        return board[:][:]
    
    def get_shot_density(self):
        if(self.last_row < 0 or self.last_row >= board_size or self.last_col < 0 or self.last_col >= board_size):
            return 0.0
        return self.prob_board[self.last_row * board_size + self.last_col]
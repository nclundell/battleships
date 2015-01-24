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

    def place_ship(self, length, marker):
        for i in range (len(self.board[0])):
            if self.ship_board[i][0] == WATER:
                for j in range(length):
                    self.ship_board[i][j] = marker
                break
    
    def mark_shot(self, shot, result):
        self.ship_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.ship_board = [["W"]*board_size for i in range(board_size)]
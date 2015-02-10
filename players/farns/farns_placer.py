#@author Nathan Lundell
#@date January 2015
#@player farns
#
#Ship Placer for @player
#
#
#

import sys
import random

sys.path.append("../../")

from b_globals import *
from b_functions import *

class FarnsworthPlacer:
    def __init__(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[0]*board_size for i in range(board_size)]

    def place_ship(self, length, ship_num):
        horizontal_cost = sys.maxsize
        vertical_cost = sys.maxsize
        h_row = 0
        h_col = 0
        v_row = 0
        v_col = 0
        #Calc min Horizontal Cost
        for i in range(board_size):
            for j in range(int(board_size/2)-1):
                cost, valid = self.get_cost(i, j, 0, length)
                if((int(cost) < horizontal_cost) and valid):
                    horizontal_cost = cost
                    h_row = i
                    h_col = j
        #Calc min Vertical Cost
        for i in range(int(board_size/2)-1):
            for j in range(board_size):
                cost, valid = self.get_cost(i, j, 1, length)
                if((cost < vertical_cost) and valid):
                    vertical_cost = cost
                    v_row = i
                    v_col = j
        if(horizontal_cost <= vertical_cost):
            for i in range(length):
                self.ship_board[h_row][h_col+i] = ship_num
        else:
            for i in range(length):
                self.ship_board[v_row+i][v_col] = ship_num
    
    def mark_shot(self, shot, result):
        self.mark_board[shot[0]][shot[1]] += 1
        
    def reset(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        
    def get_cost(self, row, col, direction, length):
        cost = 0
        if(direction == 0):
            for i in range(length):
                if(isinstance(self.ship_board[row][col+i], int)):
                    return sys.maxsize, False
                cost += self.mark_board[row][col+i]
        if(direction == 1):
            for i in range(length):
                if(isinstance(self.ship_board[row+i][col], int)):
                    return sys.maxsize, False
                cost += self.mark_board[row+i][col]
        return cost, True
#@author Nathan Lundell
#@date January 2015
#@player farnsworth
#
#Ship Placer for @player
#
#Based on Farnsworth Player by Nate Kohl
#Link: http://natekohl.net/files/FarnsworthOpponent.cs

import sys
import random

sys.path.append("../../")

from b_globals import *

class FarnsworthPlacer:
    def __init__(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[WATER]*board_size for i in range(board_size)]

    def place_ship(self, length, ship_num):
        ship_not_placed = True
        while ship_not_placed:
            row = random.randint(0, board_size-1)
            col = random.randint(0, board_size-1)
            direction = random.randint(1,4)
            
            #If Up
            if(direction == 1 and (row-length >= 0) and self.valid_placement(row, col, length, direction)):
                for i in range(length):
                    self.ship_board[row-i][col] = ship_num
                ship_not_placed = False
            #If Right
            elif(direction == 2 and (col+length <= board_size) and self.valid_placement(row, col, length, direction)):
                for i in range(length):
                    self.ship_board[row][col+i] = ship_num
                ship_not_placed = False
            #If Down
            elif(direction == 3 and (row+length <= board_size) and self.valid_placement(row, col, length, direction)):
                for i in range(length):
                    self.ship_board[row+i][col] = ship_num
                ship_not_placed = False
            #If Left
            elif(direction == 4 and (col-length >= 0) and self.valid_placement(row, col, length, direction)):
                for i in range(length):
                    self.ship_board[row][col-i] = ship_num
                ship_not_placed = False
        
    def mark_shot(self, shot, result):
        self.mark_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.ship_board = [[WATER]*board_size for i in range(board_size)]
        self.mark_board = [[WATER]*board_size for i in range(board_size)]
        
    def valid_placement(self, row, col, length, direction):
        #Check Up
        if(direction == 1):
            for i in range(length):
                if(isinstance(self.ship_board[row-i][col], int)):
                    return False
            return True
        #Check Right
        elif(direction == 2):
            for i in range(length):
                if(isinstance(self.ship_board[row][col+i], int)):
                    return False
            return True
        #Check Down
        elif(direction == 3):
            for i in range(length):
                if(isinstance(self.ship_board[row+i][col], int)):
                    return False
            return True
        #Check Left
        elif(direction == 4):
            for i in range(length):
                if(isinstance(self.ship_board[row][col-i], int)):
                    return False
            return True
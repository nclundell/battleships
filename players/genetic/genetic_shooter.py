#@author Nathan Lundell
#@date January 2015
#@player genetic
#
#Target and Shoot for @player

import sys
import math
import random

sys.path.append("../../")

from b_globals import *

class genetic_shooter:
    def __init__(self):
        self.shot_board = [[WATER]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0
        self.wins = 0
    
    def make_shot(self): 
        return [self.last_row, self.last_col]
    
    def mark_shot(self, shot, result):
        self.shot_board[shot[0]][shot[1]] = result
        
    def reset(self):
        self.shot_board = [["W"]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0

class shoot_fourier:
    def __init__(self):
        pass
    def dft(self, direction, m, x1, y1):
        pass
    def select_top(self, arr):
        top = []
        copy = arr[:]
        high = 0
        high_index = 0
        for i in range (wave_count):
            for j in range(math.pow(board_size, 2)/2):
                if(abs(copy[j] > high)):
                    high = abs(copy[j])
                    high_index = j
            top[i] = high_index
            copy[high_index] = 0
            high = 0
            high_index = 0
        return top
    
class shoot_harmonic:
    def __init__(self):
        self.step = (board_size / math.pi)
        self.dist = []
        self.alpha
        self.beta
        self.mu
        self.omega
    def harmonic(self):
        self.alpha = 0
        self.beta = 0
        self.mu = 0
        self.omega = 0
    def harmonic(self, amplitude):
        self.alpha = amplitude - 2 * random.random() * amplitude
        self.beta = amplitude - 2 * random.random() * amplitude
        self.mu = (random.randint() % 48) + 1
        self.omega = (random.randint() % 48) + 1
    def get_distrubution(self):
        for i in range(math.pow(board_size, 2)):
            self.dist[i] = self.alpha * math.sin(self.mu * (i*self.step)) + self.beta * math.cos(self.omega * (i/self.step))
        return self.dist
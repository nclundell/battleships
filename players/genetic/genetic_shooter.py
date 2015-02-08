#@author Nathan Lundell
#@date January 2015
#@player genetic
#
#Target and Shoot for @player
#
#Based on "Battlestar-AI" Project by Jeremy G. Bridon, Zachary A. Correll, Craig R. Dubler, and  Zachary K. Gotsch
#Link: https://code.google.com/p/battlestar-ai/

import sys
import math
import random

sys.path.append("../../")

from b_globals import *

wave_count = board_size
mutation_rate = 0.1
max_scaled_sin_cos = 10000

class GeneticShooter:
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
        self.shot_board = [[WATER]*self.board_size for i in range(self.board_size)]
        self.last_row = 0
        self.last_col = 0

class GAShoot:
    @classmethod
    def target(cls, target):
        shoot = cls()
        return shoot
    
    @classmethod
    def enemy(cls, enemy_name):
        shoot = cls()
        return shoot

class GenePool:
    @classmethod
    def none(cls):
        pool = cls()
        pool.increment = 1
        return pool
    
    @classmethod
    def target(cls, target):
        pool = cls()
        pool.increment = 1
        return pool
    
    def advance(self):
        pass
    
    def best(self):
        pass
    
    def save(self, file_name):
        pass
    
    def load(self, file_name):
        pass
    
    def get_target(self, x, y, board):
        pass
    
    def best_fitness(self):
        pass
    
    def best_dist(self):
        pass
    
    def get_perfect(self):
        pass
    
    def save_hit(self, x, y):
        pass
    
    

class Gene:
    @classmethod
    def none(cls):
        gene = cls()
        gene.waves = []
        gene.magnitude = 0
        for i in range(wave_count):
            gene.waves[i] = Harmonic.amplitude(max_scaled_sin_cos)
        return gene
    
    @classmethod
    def magnitude(cls, magnitude):
        gene = cls()
        gene.waves = []
        gene.magnitude = magnitude
        for i in range(wave_count):
            gene.waves[i] = Harmonic.amplitude(max_scaled_sin_cos)
        return gene
    
    @classmethod
    def harmonics(cls, waves):
        gene = cls()
        gene.waves = waves[:]
        return gene
    
    @classmethod
    def mag_harm(cls, magnitude, waves):
        gene = cls()
        gene.magnitude = magnitude
        gene.waves = waves[:]
        return gene
    
    def get_dist(self):
        dist = []
        for i in range(math.pow(bard_size, 2)):
            dist.append(self.magnitude)
        for i in range(wave_count):
            wave_dist = waves[i].get_dist()
            for j in range(math.pow(board_size, 2)):
                dist[j] += wave_dist[j]
        return dist[:]
        
    def fitness(target):
        pass
        
    def gene_cross(father, mother, mutate): ##Incomplete!!!!
        perfect_child = []
        father_dist = father.get_dist()
        mother_dist = mother.get_dist()
        
        for i in range(math.pow(board_size, 2)):
            perfect_child.append((father_dist[i] + mother_dist[i]) / 2)
        
        imaginary = [[0]*self.board_size for i in range(self.board_size)]
        
        succeed = fourier.dft(1, math.pow(board_size, 2), perfect_child, imaginary)
        if(not succeed):
            sys.exit(0)
            
        sines = fourier.select_top(imaginary)
        cosines = fourier.select_top(perfect_child)
        
        waves = []
        for i in range(wave_count):
            alpha = mutate
            beta = mutate
            mu = mutate
            omega = mutate
            waves.append(Harmonic.set(alpha, beta, mu, omega))
        
        return Gene.mag_harm(magnitude, waves)
        
class Fourier:
    def __init__(self):
        pass
    
    def dft(self, direction, m, x, y):
        for i in range(m):
            arg = -direction * 2 * math.pi * i / m
            for j in range(m):
                sinarg = math.sin(k * arg)
                cosarg = math.cos(k * arg)
                x[i] = x[j] * cosarg - y[j] * sinarg
                y[i] = x[j] * sinarg + y[j] * cosarg
        return True
        
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
            top.apped(high_index)
            copy[high_index] = 0
            high = 0
            high_index = 0
        return top
    
class Harmonic:
    @classmethod    
    def none(cls):
        harmonic = cls()
        harmonic.alpha = 0
        harmonic.beta = 0
        harmonic.mu = 0
        harmonic.omega = 0
        return harmonic
        
    @classmethod    
    def amplitude(cls, amplitude):
        harmonic = cls()
        harmonic.alpha = amplitude - 2 * random.random() * amplitude
        harmonic.beta = amplitude - 2 * random.random() * amplitude
        harmonic.mu = (random.randint() % 48) + 1
        harmonic.omega = (random.randint() % 48) + 1
        return harmonic
    
    @classmethod    
    def set(cls, alpha, beta, mu, omega):
        harmonic = cls()
        harmonic.alpha = alpha
        harmonic.beta = beta
        harmonic.mu = mu
        harmonic.omega = omega
        return harmonic
    
    def get_dist(self):
        dist = []
        step = math.pow(board_size, 2) / (2 * math.pi)
        for i in range(math.pow(board_size, 2)):
            self.dist.append(self.alpha * math.sin(self.mu * (i*step)) + self.beta * math.cos(self.omega * (i/self.step)))
        return self.dist

 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import os
import time
from b_functions import *
from b_globals import *

#Import Players
sys.path.append("players/chance")
sys.path.append("players/dumb")
sys.path.append("players/genetic")

from chance_placer import *
from chance_shooter import *
from dumb_placer import *
from dumb_shooter import *
from genetic_placer import *
from genetic_shooter import *

#Game Variables
ships = [CARRIER, BATTLESHIP, SUBMARINE, DESTROYER, CRUISER]
default = "dumb"
board_size = 10

#Clear Screen
clear()

#Get/Check Command Line Arguments
p1_placer_choice, p1_name, p2_placer_choice, p2_name, rounds = command_args(sys.argv)
p1_shooter_choice, p2_shooter_choice = "-c"

#Check for Placer File
if(p1_placer_choice == "-c" and custom_placer_check(p1_name)):
    print "Placer found for",p1_name
else:
    print "Placer not found for",p1_name
    print "Using default placer for",p1_name
    p1_placer_choice = "-d"
    
if(p2_placer_choice == "-c" and custom_placer_check(p2_name)):
    print "Placer found for",p2_name
else:
    print "Placer not found for",p2_name
    print "Using default placer for",p2_name
    p2_placer_choice = "-d"

#Move to Next Check
time.sleep(3)
clear()

#Check for Shooter File
if(custom_shooter_check(p1_name)):
    print "Shooter found for",p1_name
else:
    print "Shooter not found for",p1_name
    print "Using default shooter for",p1_name
    p1_shooter_choice = "-d"
    
if(custom_shooter_check(p2_name)):
    print "Shooter found for",p2_name
else:
    print "Shooter not found for",p2_name
    print "Using default shooter for",p2_name
    p2_shooter_choice = "-d"

#Move to Next Check
time.sleep(3)
clear()

#Wait To Read Notice
if(p1_placer_choice == "-d" or p2_placer_choice == "-d"):
    print "Notice: Using %s player as default!" %default
    time.sleep(3)
    clear()

#Instantiate Player 1 Placer
if(p1_placer_choice == "-c"):
    if(p1_name == "chance"):
        p1_placer = chance_placer(board_size)
    if(p1_name == "dumb"):
        p1_placer = dumb_placer(board_size)
    if(p1_name == "genetic"):
        p1_placer = genetic_placer(board_size)
else:
    p1_placer = dumb_placer(board_size)

#Instantiate Player 2 Placer
if(p2_placer_choice == "-c"):
    if(p2_name == "chance"):
        p2_placer = chance_placer(board_size)
    if(p2_name == "dumb"):
        p2_placer = dumb_placer(board_size)
    if(p2_name == "genetic"):
        p2_placer = genetic_placer(board_size)
else:
    p2_placer = dumb_placer(board_size)
    
#Instantiate Player 1 Shooter 
if(p1_shooter_choice == "-c"):
    if(p1_name == "chance"):
        p1_shooter = chance_shooter(board_size)
    if(p1_name == "dumb"):
        p1_shooter = dumb_shooter(board_size)
    if(p1_name == "genetic"):
        p1_shooter = genetic_shooter(board_size)
else:
    p1_shooter = dumb_shooter(board_size)

#Instantiate Player 2 Shooter 
if(p2_shooter_choice == "-c"):
    if(p2_name == "chance"):
        p2_shooter = chance_shooter(board_size)
    if(p2_name == "dumb"):
        p2_shooter = dumb_shooter(board_size)
    if(p2_name == "genetic"):
        p2_shooter = genetic_shooter(board_size)
else:
    p2_shooter = dumb_shooter(board_size)

#Start Contest
for r in range(rounds):
    #Place Ships in Ship List
    for s in range(len(ships)):
        p1_placer.place_ship(ships[s][0], ships[s][1])
        p2_placer.place_ship(ships[s][0], ships[s][1])
    #Validate Boards
    
    game_over = False
    while(game_over != True):

        #Get Shots
        p1_shot = p1_shooter.make_shot()
        p2_shot = p2_shooter.make_shot()
        
        #Mark Shot 1
        if(p2_placer.board[p1_shot[0]][p1_shot[1]] == WATER):
            p2_placer.mark_shot(p1_shot, MISS)
            p1_shooter.mark_shot(p1_shot, MISS)
        else:
            p2_placer.mark_shot(p1_shot, HIT)
            p1_shooter.mark_shot(p1_shot, HIT)
        
        #Mark Shot 2
        if(p1_placer.board[p2_shot[0]][p2_shot[1]] == WATER):
            p1_placer.mark_shot(p2_shot, MISS)
            p2_shooter.mark_shot(p2_shot, MISS)
        else:
            p1_placer.mark_shot(p2_shot, HIT)
            p2_shooter.mark_shot(p2_shot, HIT)
            
        #Print Boards to Screen
        print "Game #"+str(r+1)+"\n"
        print "Player 1 Shots: 							Player 2 Shots:"
        for i in range(board_size):
            print p1_shooter.board[i],"\t\t\t",p2_shooter.board[i]
        
        #Print Shot Result
        if(p1_shooter.board[p1_shot[0]][p1_shot[1]] == HIT):
            print "\n Player 1 Hit! "+str(p1_shot)
        else:
            print "\n Player 1 Miss! "+str(p1_shot)
            
        if(p2_shooter.board[p1_shot[0]][p2_shot[1]] == HIT):
            print "\n Player 2 Hit! "+str(p2_shot)
        else:
            print "\n Player 2 Miss! "+str(p2_shot)
        
        #Check for Game Over
        winner = check_game_over(p1_placer.board, p2_placer.board, board_size)
        if(winner == "NONE"):
            game_over = False
        if(winner == "TIE"):
            game_over = True
        if(winner == "P1"):
            game_over = True
            p1_shooter.wins += 1
        if(winner == "P2"):
            game_over = True
            p2_shooter.wins += 1
        
        #Pause For Next Shot
        time.sleep(0)
        clear()
    
    #Reset For Next Game
    p1_placer.reset()
    p2_placer.reset()
    p1_shooter.reset()
    p2_shooter.reset()

print p1_shooter.wins
print p2_shooter.wins

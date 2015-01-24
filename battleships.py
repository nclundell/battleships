 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import os
import time
from b_functions import *
from b_globals import *

#Import Players
sys.path.append("players/prob")
sys.path.append("players/dumb")
sys.path.append("players/genetic")

from prob_placer import *
from prob_shooter import *
from dumb_placer import *
from dumb_shooter import *
from genetic_placer import *
from genetic_shooter import *

#Clear Screen
clear()

#Get/Check Command Line Arguments
p1_placer_choice, p1_name, p2_placer_choice, p2_name, rounds = command_args(sys.argv)

#Check for Placer File
if(p1_placer_choice == "-c" and custom_placer_check(p1_name)):
    print "Placer found for",p1_name
elif(p1_placer_choice == "-c" and not custom_placer_check(p1_name)):
    print "Placer not found for",p1_name
    print "Using default placer for",p1_name
    p1_placer_choice = "-d"
else:
    print "Using default placer for",p1_name
    
if(p2_placer_choice == "-c" and custom_placer_check(p2_name)):
    print "Placer found for",p2_name
elif(p2_placer_choice == "-c" and not custom_placer_check(p2_name)):
    print "Placer not found for",p2_name
    print "Using default placer for",p2_name
    p2_placer_choice = "-d"
else:
    print "Using default placer for",p2_name

#Move to Next Check
sleep(3)
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
sleep(3)
clear()

#Wait To Read Notice
if(p1_placer_choice == "-d" or p2_placer_choice == "-d"):
    print "Notice: Using %s player as default!" %default
    sleep(3)
    clear()

#Instantiate Player 1 Placer
if(p1_placer_choice == "-c"):
    if(p1_name == "prob"):
        p1_placer = prob_placer()
    if(p1_name == "dumb"):
        p1_placer = dumb_placer()
    if(p1_name == "genetic"):
        p1_placer = genetic_placer()
    ##Add New Player here!!!!!
    #elif(p1_name == "[name]"):
    #    p1_placer = [name]_placer()
else:
    print "Using default ship placer for Player 1"
    p1_placer = dumb_placer()
    time.sleep(3)
    clear()
    
#Instantiate Player 2 Placer
if(p2_placer_choice == "-c"):
    if(p2_name == "prob"):
        p2_placer = prob_placer()
    if(p2_name == "dumb"):
        p2_placer = dumb_placer()
    if(p2_name == "genetic"):
        p2_placer = genetic_placer()
    ##Add New Player here!!!!!
    #elif(p2_name == "[name]"):
    #    p2_placer = [name]_placer()
else:
    print "Using default ship placer for Player 2"
    p2_placer = dumb_placer()
    time.sleep(3)
    clear()
    
#Instantiate Player 1 Shooter 
if(p1_name == "prob"):
    p1_shooter = prob_shooter()
elif(p1_name == "dumb"):
    p1_shooter = dumb_shooter()
elif(p1_name == "genetic"):
    p1_shooter = genetic_shooter()
##Add New Player here!!!!!
#elif(p1_name == "[name]"):
#    p1_shooter = [name]_shooter()
else:
    print "Using default shooter for Player 1"
    p1_shooter = dumb_shooter()
    time.sleep(3)
    clear()

#Instantiate Player 2 Shooter 
if(p2_name == "prob"):
    p2_shooter = prob_shooter()
elif(p2_name == "dumb"):
    p2_shooter = dumb_shooter()
elif(p2_name == "genetic"):
    p2_shooter = genetic_shooter()
##Add New Player here!!!!!
#elif(p2_name == "[name]"):
#    p2_shooter = [name]_shooter()
else:
    print "Using default shooter for Player 2"
    p2_shooter = dumb_shooter()
    time.sleep(3)
    clear()

#Start Contest
for r in range(rounds):
    #Place Ships in Ship List
    for s in range(len(ships)):
        p1_placer.place_ship(ships[s], s)
        p2_placer.place_ship(ships[s], s)
        
    #Validate Boards
    p1_valid = valid_board(p1_placer.ship_board)
    p2_valid = valid_board(p2_placer.ship_board)
    
    if not p1_valid:
        print "Player 1 has invalid ship placement"
        sys.exit(0)
    if not p2_valid:
        print "Player 2 has invalid ship placement"
        sys.exit(0)
    if(print_games):
        print "Valid ship placements"    
        sleep(3)
        clear()
        
    game_over = False
    while(game_over != True):

        #Get Shots
        p1_shot = p1_shooter.make_shot()
        p2_shot = p2_shooter.make_shot()
        
        #Mark Shot 1
        if(p2_placer.ship_board[p1_shot[0]][p1_shot[1]] == WATER or p2_placer.ship_board[p1_shot[0]][p1_shot[1]] == KILL):
            p2_placer.mark_shot(p1_shot, MISS)
            p1_shooter.mark_shot(p1_shot, MISS)
        else:
            p2_placer.mark_shot(p1_shot, HIT)
            p1_shooter.mark_shot(p1_shot, HIT)
        
        #Mark Shot 2
        if(p1_placer.ship_board[p2_shot[0]][p2_shot[1]] == WATER or p1_placer.ship_board[p2_shot[0]][p2_shot[1]] == KILL):
            p1_placer.mark_shot(p2_shot, MISS)
            p2_shooter.mark_shot(p2_shot, MISS)
        else:
            p1_placer.mark_shot(p2_shot, HIT)
            p2_shooter.mark_shot(p2_shot, HIT)
        
        if(print_games):
            #Print Boards to Screen
            print "Game #"+str(r+1)+"\n"
            print "Player 1 Shots: 							Player 2 Shots:"
            print "    0    1    2    3    4    5    6    7    8    9                          0    1    2    3    4    5    6    7    8    9"
            print "   ------------------------------------------------                        ------------------------------------------------"
            for i in range(board_size):
                print i,p1_shooter.shot_board[i],"\t\t\t",i,p2_shooter.shot_board[i],"\n"
            
            #Print Shot Result
            if(p1_shooter.shot_board[p1_shot[0]][p1_shot[1]] == HIT):
                print "\n Player 1 Hit! "+str(p1_shot)
                if(is_sunk(p2_placer.ship_board[p1_shot[0]][p1_shot[1]], p2_placer.ship_board, p1_shooter.shot_board) == True):
                    mark_kill(p2_placer.ship_board[p1_shot[0]][p1_shot[1]], p2_placer.ship_board, p1_shooter.shot_board)
            else:
                print "\n Player 1 Miss! "+str(p1_shot)
                
            if(p2_shooter.shot_board[p1_shot[0]][p2_shot[1]] == HIT):
                print "\n Player 2 Hit! "+str(p2_shot)
                if(is_sunk(p1_placer.ship_board[p2_shot[0]][p2_shot[1]], p1_placer.ship_board, p2_shooter.shot_board) == True):
                    mark_kill(p1_placer.ship_board[p2_shot[0]][p2_shot[1]], p1_placer.ship_board, p2_shooter.shot_board)
            else:
                print "\n Player 2 Miss! "+str(p2_shot)
            
        #Check for Game Over
        winner = check_game_over(p1_placer.ship_board, p2_placer.ship_board, board_size)
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
        
        if(print_games):
            #Pause For Next Shot
            sleep(1)
            clear()
        
    #Reset For Next Game
    p1_placer.reset()
    p2_placer.reset()
    p1_shooter.reset()
    p2_shooter.reset()

#Print Results
print "Player 1 wins:",p1_shooter.wins
print "Player 2 wins:",p2_shooter.wins
print "Player 1 shot average:",average_shot_count(p1_shooter.shot_records)
print "Player 2 shot average:",average_shot_count(p2_shooter.shot_records)


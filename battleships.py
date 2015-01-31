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

#from prob_placer import *
from prob_shooter import *
from dumb_placer import *
from dumb_shooter import *
from genetic_placer import *
from genetic_shooter import *

#Clear Screen
clear()

#Get/Check Command Line Arguments
p1_name, p2_name, rounds = command_args(sys.argv)

#Instantiate Player 1
if(player_exists(p1_name)):
    #Player 1 Placer
    if(custom_placer_check(p1_name)):
        if(p1_name == "prob"):
            p1_placer = prob_placer()
        elif(p1_name == "dumb"):
            p1_placer = dumb_placer()
        elif(p1_name == "genetic"):
            p1_placer = genetic_placer()
        ##Add New Player here!!!!!
        #elif(p1_name == "[name]"):
        #    p1_placer = [name]_placer()
    else:
        p1_placer = dumb_placer()
        using_default = True
    #Player 1 Shooter
    if(custom_shooter_check(p1_name)):
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
        p1_shooter = dumb_shooter()
        using_default = True
else:
    sys.exit(0)
    
#Instantiate Player 2
if(player_exists(p2_name)):
    #Player 2 Placer
    if(custom_placer_check(p2_name)):
        if(p2_name == "prob"):
            p2_placer = prob_placer()
        elif(p2_name == "dumb"):
            p2_placer = dumb_placer()
        elif(p2_name == "genetic"):
            p2_placer = genetic_placer()
        ##Add New Player here!!!!!
        #elif(p2_name == "[name]"):
        #    p2_placer = [name]_placer()
    else:
        p2_placer = dumb_placer()
        using_default = True
    #Player 2 Shooter
    if(custom_shooter_check(p2_name)):
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
        p2_shooter = dumb_shooter()
        using_default = True   
else:
    sys.exit(0)

#Print Default Notice
if(using_default):
    print "Notice: Using %s player as default!" %default
#Pause before Start Game
sleep(3)
clear()

shots_per_game = []
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

    game_shots = 0
    game_over = False
    while(game_over != True):
        #Get Shots
        p1_shot = p1_shooter.make_shot(game_shots)
        if isinstance(p1_shot, str):
            print "p1_shot is a string!"
            pause()
        p2_shot = p2_shooter.make_shot(game_shots)
        if isinstance(p2_shot, str):
            print "p2_shot is a string!"
            pause()
        game_shots += 1
        
        #Mark Shot 1
        #if(p2_placer.ship_board[p1_shot[0]][p1_shot[1]] == WATER or p2_placer.ship_board[p1_shot[0]][p1_shot[1]] == KILL):
        if(p2_placer.ship_board[p1_shot[0]][p1_shot[1]] == WATER):
            p2_placer.mark_shot(p1_shot, MISS)
            p1_shooter.mark_shot(p1_shot, MISS)
        else:
            p2_placer.mark_shot(p1_shot, HIT)
            p1_shooter.mark_shot(p1_shot, HIT)
        
        #Mark Shot 2
        #if(p1_placer.ship_board[p2_shot[0]][p2_shot[1]] == WATER or p1_placer.ship_board[p2_shot[0]][p2_shot[1]] == KILL):
        if(p1_placer.ship_board[p2_shot[0]][p2_shot[1]] == WATER):
            p1_placer.mark_shot(p2_shot, MISS)
            p2_shooter.mark_shot(p2_shot, MISS)
        else:
            p1_placer.mark_shot(p2_shot, HIT)
            p2_shooter.mark_shot(p2_shot, HIT)
        
        if isinstance(p1_shot, str):
            print "test2: p1_shot is a string!"
            pause()
        if isinstance(p2_shot, str):
            print "test2: p2_shot is a string!"
            pause()
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
                if(is_sunk(p1_shot, p2_placer.ship_board, p1_shooter.shot_board)):
                    p1_shooter.kills += 1
            else:
                print "\n Player 1 Miss! "+str(p1_shot)
                
            if(p2_shooter.shot_board[p2_shot[0]][p2_shot[1]] == HIT):
                print "\n Player 2 Hit! "+str(p2_shot)
                if(is_sunk(p2_shot, p1_placer.ship_board, p2_shooter.shot_board)):
                    p2_shooter.kills += 1
            else:
                print "\n Player 2 Miss! "+str(p2_shot)
        
        if(not print_games):
            #Shot Result
            if(p1_shooter.shot_board[p1_shot[0]][p1_shot[1]] == HIT):
                if(is_sunk(p1_shot, p2_placer.ship_board, p1_shooter.shot_board)):
                    p1_shooter.kills += 1
                
            if(p2_shooter.shot_board[p2_shot[0]][p2_shot[1]] == HIT):
                if(is_sunk(p2_shot, p1_placer.ship_board, p2_shooter.shot_board)):
                    p2_shooter.kills += 1
            
        #Check for Game Over
        winner = check_game_over(p1_shooter.kills, p1_shooter.wins, p2_shooter.kills, p2_shooter.wins)
        if(winner == "P1"):
            p1_shooter.wins += 1
            game_over = True
        elif(winner == "P2"):
            p2_shooter.wins += 1
            game_over = True
        elif(winner == "TIE"):
            game_over = True

        if(print_games):
            #Pause For Next Shot
            sleep(1)
            clear()
            
    #Reset For Next Game
    p1_placer.reset()
    p2_placer.reset()
    p1_shooter.reset()
    p2_shooter.reset()
    shots_per_game.append(game_shots)
    game_shots = 0

#Print Results
print "Player "+p1_name+" wins:"+str(p1_shooter.wins)+"/"+str(rounds)
print "Player "+p2_name+" wins:"+str(p2_shooter.wins)+"/"+str(rounds)
print "Shot Average:",average_shot_count(shots_per_game)

##Make folder "results/" before uncommenting.
#export_shot_records(p1_name, p2_name, shots_per_game)


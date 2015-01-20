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
time.sleep(5)
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
time.sleep(5)
clear()

#Wait To Read Notice
if(p1_placer_choice == "-d" or p2_placer_choice == "-d"):
    print "Notice: Using %s player as default!" %default
    time.sleep(5)
    clear()

#Make Boards
p1_ship_board = [["W"]*board_size for i in range(board_size)]
p1_shot_board = [["W"]*board_size for i in range(board_size)]
p2_ship_board = [["W"]*board_size for i in range(board_size)]
p2_shot_board = [["W"]*board_size for i in range(board_size)]

#Instantiate Player 1 Placer
if(p1_placer_choice == "-c"):
    if(p1_name == "chance"):
        p1_placer = chance_placer(p1_ship_board)
    if(p1_name == "dumb"):
        p1_placer = dumb_placer(p1_ship_board)
    if(p1_name == "genetic"):
        p1_placer = genetic_placer(p1_ship_board)
else:
    p1_placer = dumb_placer(board_sp1_ship_boardize)

#Instantiate Player 2 Placer
if(p2_placer_choice == "-c"):
    if(p2_name == "chance"):
        p2_placer = chance_placer(p2_ship_board)
    if(p2_name == "dumb"):
        p2_placer = dumb_placer(p2_ship_board)
    if(p2_name == "genetic"):
        p2_placer = genetic_placer(p2_ship_board)
else:
    p2_placer = dumb_placer(p2_ship_board)
    
##Instantiate Player 1 Shooter 
#if(p1_shooter_choice == "-c"):
#    if(p1_name == "chance"):
#        p1_shooter = chance_shooter()
#    if(p1_name == "dumb"):
#        p1_shooter = dumb_shooter()
#    if(p1_name == "genetic"):
#        p1_shooter = genetic_shooter()
#else:
#    p1_shooter = dumb_shooter()
#
##Instantiate Player 2 Shooter 
#if(p2_shooter_choice == "-c"):
#    if(p2_name == "chance"):
#        p2_shooter = chance_shooter()
#    if(p2_name == "dumb"):
#        p2_shooter = dumb_shooter()
#    if(p2_name == "genetic"):
#        p2_shooter = genetic_shooter()
#else:
#    p2_shooter = dumb_shooter()

#Make Boards
p1_ship_board = [["W"]*board_size for i in range(board_size)]
p1_shot_board = [["W"]*board_size for i in range(board_size)]
p2_ship_board = [["W"]*board_size for i in range(board_size)]
p2_shot_board = [["W"]*board_size for i in range(board_size)]

#Start Contest
#for i in range(rounds):
#    print i
#Place Ships in Ship List
for i in range(len(ships)):
    p1_placer.place_ship(ships[i][0], ships[i][1])
    p2_placer.place_ship(ships[i][0], ships[i][1])

#Get Boards
p1_ship_board = p1_placer.get_board()
p2_ship_board = p2_placer.get_board()

print p1_ship_board
print p2_ship_board

  

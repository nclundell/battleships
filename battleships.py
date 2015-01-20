 #@author Nathan Lundell
 #@date January 2015
 #Main runner for Battleships simulator

import sys
import socket
import os
import b_functions

#Clear Screen
b_functions.clear()

#Get/Check Command Line Arguments
p1Placer, p1Name, p2Placer, p2Name, rounds = b_functions.command_args(sys.argv)

#Check for Placer File
p1Placer = b_functions.custom_placer_check(p1Placer, p1Name, b_functions.custom_placer_path(p1Name))
p2Placer = b_functions.custom_placer_check(p2Placer, p2Name, b_functions.custom_placer_path(p2Name))

b_functions.pause()
b_functions.clear()

#Start Contest Manager
os.system("python2 contest_manager.py "+p1Name+" "+p2Name+" "+"10")   

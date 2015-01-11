/**
 *@author Nathan Lundell
 *@date January 2015
 *Main runner for Battleships simulator
 *
 *
**/
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "main.h"

using namespace std;

int main(int argc, char *argv[]){

//Get Commandline variable values
place1 = argv[1];
player1 = argv[2];
place2 = argv[3];
player2 = argv[4];
if(argc==6)
    rounds = argv[5];


//Check for valid players
if(!validPlayer(player1)){
    cout<<"Player1 does not exist: "<<player1;
    return 0;
}
if(!validPlayer(player2)){
    cout<<"Player2 does not exist: "<<player2;
    return 0;
}

//Run Ship Placement Checker for each custom placer
    //if(!checkPlacement(player#Placement))
        //Exit with Error
//Run match simulator
    //runMatch(player1Placement, player1Shooter,player2Placement, player2Shooter);

//Print Results
    return 0;
}

bool validPlayer(string name){
    string entry = "";
    ifstream playerList
    playerList.open("players/playerList.csv")
    while(getline(playerList, entry)){
        if(entry == name)
            return true;
    }
    return false;
}

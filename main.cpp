/**
 *@author Nathan Lundell
 *@date January 2015
 *Main runner for Battleships simulator
 *
 *
**/
#include <iostream>
#include <list>
#include "main.h"

using namespace std;

int main(){
//Get Players
list players = getPlayers();



//Pick Game Type
    //1. Player vs. Player
    //2. Player vs. Computer
    //3. Computer vs. Computer

//Pick number of rounds

//Given game type, pick players

//Run Ship Placement Checker for each custom placer
    //if(!checkPlacement(player#Placement))
        //Exit with Error
//Run match simulator
    //runMatch(player1Placement, player1Shooter,player2Placement, player2Shooter);

//Print Results
    return 0;
}

list getPlayers(){
    //Define Variables
    list<struct> players;
    struct player{
        string name;
        string type;
        string shipPlacer;
        string title;
    };
    string entry;

    //Build Player List from File
    ifstream readPlayers("players/playerList.csv");
    while(readPlayers){
        getline(readPlayers, entry);
        //Split Entry and Add to Struct
    }

    //Drop CSV Titles
    players.pop_front();

    //Return List of Players
    return players;
}

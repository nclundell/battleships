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
#include <string>
#include "main.h"

using namespace std;

int main(int argc, char *argv[]){

//Get Commandline variable values
char place1 = *argv[1];
string player1 = argv[2];
char place2 = *argv[3];
string player2 = argv[4];
if(argc==6){
    int rounds = atoi(argv[5]);
}

//Check for valid players
if(!validPlayer(player1)){
    cout<<"Player1 does not exist: "<<player1;
    return 0;
}
if(!validPlayer(player2)){
    cout<<"Player2 does not exist: "<<player2;
    return 0;
}


//Check for ship placer
if(place1 == 'c'){
    if(!existsPlacer(player1)){
        cout<<"Player1 does not have a ship placer.";
        return 0;
    }
}
if(place2 == 'c'){
    if(!existsPlacer(player2)){
        cout<<"Player2 does not have a ship placer.";
        return 0;
    }
}

//Run match simulator
    //runMatch(player1Placement, player1Shooter,player2Placement, player2Shooter);

//Print Results

    return 0;
}

bool validPlayer(string name){
    string entry = "";
    ifstream playerList;
    playerList.open("players/playerList.csv");
    while(getline(playerList, entry)){
        if(entry == name){
            playerList.close();
            return true;
        }
    }
    playerList.close();
    return false;
}

bool existsPlacer(string name){
    string placerFile = "players/player"+name+"/place"+name+".cpp";
    ifstream infile;
    infile.open(placerFile.c_str());
    if(infile){
        infile.close();
        return true;
    }
    infile.close();
    return false;
}

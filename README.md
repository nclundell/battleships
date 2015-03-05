# Battleships Project: JTerm 2015

###Goals:
1) Simulate Battleship games using artificially intelligent players.<br/>

===================
###Run Battleships:
Run Battleships with the following cli command:
```
   python battleships.py [p1_name] [p2_name] [rounds (optional)]
```
For example, if you wanted to run the Dumb player against the Genetic player for 75 rounds:
```
   python battleships.py dumb genetic 75
```
Note: Battleships requires Python >= 3.4

======================
###Defaults:
<ul>
   <li>
      Rounds: 50
   </li>
   <li>
      Placer: dumb
   </li>
   <li>
      Shooter: dumb
   </li>
   <li>
      Board Size: 10
   </li>
   <li>
      Ship List: Carrier, Battleship, Submarine, Destroyer, Cruiser
   </li>
</ul>
======================
###Players:
#####Computer Players:
<ol>
   <li>
      Dumb Player [dumb]
      <ul>
         <li>
            Places ships and shoots to opponent board in predefined patterns that never change.
         </li>
      </ul>
   </li>
   <li>
      Probability Player [prob]
      <ul>
         <li>
            Places ships and shoots to opponent board based on probabilities calculated for each spot on the board.
         </li>
      </ul>
   </li>
   <li>
      Farnsworth Player [farns]
      <ul>
         <li>
            Uses tree-based searching of "heat map" states to get next shots.
         </li>
         <li>
            Based on Nate Kohl's "Farnsworth Opponent": http://natekohl.net/files/FarnsworthOpponent.cs
         </li>
      </ul>
   </li>
</ol>

#####Additional Players:
Additional players can be added via the following steps:
<ol>
   <li>
      Add a new folder [name] into the players folder.
   </li>
   <li>
      Add [name]_placer.py and [name]_shooter.py files into your new folder.
         <ul>
            <li>
               Default placer or shooter will be used if a file is missing or misnamed.
            </li>
         </ul>
   </li>
   <li>
      Add [name]_placer.py and [name]_shooter.py to import list at top of battleships.py
   </li>
   <li>
      Add relevant code to instantiation sections of battleships.py
   </li>
   <li>
      Add [name] to list of players in b_globals.py
   </li>
</ol>

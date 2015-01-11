# Battleships Project: JTerm 2015
Simulate Battleship games using artificially intelligent players.

===================
###Run Battleships:
```
   battleships -[placer (d|c)] [name] -[placer (d|c)] [name] [matches (optional)]
```
   For example, if you wanted to run the Dumb player with the default ship placer against the Genetic player with its custom ship placer, and run for 50 matches, the command would look like this:
```
   battleships -d Dumb -c Genetic 50
```
======================
###Players:
#####Prebuilt Players:
1) Dumb Player (In Progress)
<ul>
   <li>Places ships and shoots to opponent board in predefined patterns that never change.</li>
</ul>
2) Chance Player (In Progress)
<ul>
   <li>Places ships and shoots to opponent board based on probabilities calculated for each spot on the board.</li>
</ul>
3) Genetic Player (In Progress)
<ul>
   <li>Uses genetic algorithms to develop placing and shooting strategies.</li>
</ul>

#####Additional Players:
<ul>
   <li>
      Additional players can be added by adding a new folder player[name] into the players folder and appending [name] to the end of the playerList.csv file.
   </li>
   <li>
      Must include player[name].h and shoot[name].cpp files.
   </li>
   <li>
      The place[name].cpp file can be left out if using the default ship placer.
   </li>
</ul>

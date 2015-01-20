# Battleships Project: JTerm 2015

###Goals:
1) Simulate Battleship games using artificially intelligent players.<br/>

===================
###Run Battleships:
Run Battleships with the following cli command:
```
   battleships -[placer (d|c)] [name] -[placer (d|c)] [name] [matches (optional)]
```
For example, if you wanted to run the Dumb player with the default ship placer against the Genetic player with its custom ship placer, and run for 75 matches, the command would look like this:
```
   battleships -d Dumb -c Genetic 75
```
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
</ul>
======================
###Players:
#####Computer Players:
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
      Additional players can be added by adding a new folder [name] into the players folder.
   </li>
   <li>
      The [name]_shoot.py file can be left out if using the default shooter.
   </li>
   <li>
      The [name]_placer.py file can be left out if using the default ship placer.
   </li>
</ul>

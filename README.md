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
      Probability Player (In Progress)
      <ul>
         <li>
            Places ships and shoots to opponent board based on probabilities calculated for each spot on the board.
         </li>
      </ul>
   </li>
   <li>
      Genetic Player (In Progress)
      <ul>
         <li>
            Uses genetic algorithms to develop placing and shooting strategies.
         </li>
      </ul>
   </li>
</ol>

#####Additional Players:
<ol>
Additional players can be added via the following steps:
   <li>
      Add a new folder [name] with relevant files into the players folder.
      <ul>
         <li>
            The [name]_shoot.py file is reqired.
         </li>
         <li>
            The [name]_placer.py file can be left out if using the default ship placer.
         </li>
      </ul>
   </li>
   <li>
      Add [name]_placer.py and [name]_shooter.py to import list at top of battleships.py
   </li>
   <li>
      Add relevant code to instantiation sections of battleships.py
   </li>
</ol>

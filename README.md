# Battleships Project: JTerm 2015
Simulate Battleship games using artificially intelligent players:

<p><strong>Run Battleships:</strong></p>
```
   battleships -[placer (d|c)] [player1] -[placer (d|c)] [player2] [matches (optional)]
```
   For example, if you wanted to run the Dumb player with the default ship placer against the Genetic player with its custom ship placer, and run for 50 matches, the command would look like this:
```
   battleships -d Dumb -c Genetic 50
```

<p><strong>Players:</strong></p>
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

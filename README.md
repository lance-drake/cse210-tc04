# Hilo
How much are you willing to lose? Play <i>HiLo</i> to find out! The rules are 
simple. The dealer draws a new card. You guess if the next one will be higher or 
lower. Earn 100 points if you're right. Lose 75 if you're wrong. End the game at 
any time or just keep playing. Watch out though. Lose all your points and the 
game is ended for you!

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. 
Open a terminal and browse to the project's root folder. Start the program by 
running the following command.
```
python3 hilo 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hilo folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hilo                (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
  +-- player.py         (player for the game)
  +-- dealer.py         (game dealer)
+-- README.md           (general info)
```

## Rules 
Hilo is played according to the following rules.

  - Individual cards are represented as a number from 1 to 13.
  - The player starts the game with 300 points.
  - The dealer displays the current card.
  - The player guesses if the next one will be higher or lower.
  - The dealer shows the next card.
  - The player earns 100 points if they guessed correctly.
  - The player loses 75 points if they guessed incorrectly.
  - If a player reaches 0 points the game is over. Otherwise, the player decides whether or not to play again.
  - If a player decides not to play again the game is over.

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Lance Drake - dra15006@byui.edu
* 
* TODO: Add your names and emails here

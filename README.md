# Projects
This is a collection of the various projects and similar such things I have made throughout school and on my own time.
The wireframe and shading programs are individual iterations of a project to recreate 3d graphics from scratch using math.
The Connect 4 programs were created because I wanted to play with minimaxxing and 

Notes on how to run the programs with requirements:

Connect4Window uses an instance of Connect4AIAgent and the pygame library to run, both are require to play a game against the Agent. Running 
Connect4Window on the command line will start a game.

Gameboard allows for custom boards to be generated and played with a specified number of players, but it is not intended to work with the agent.
It will not run as a python script. This is a class intended to be implemented into other code.

TicTacToeGame works by loading the provided move dictionary text file, so both are required to run it. The dictionary can be edited to edit the behavior.

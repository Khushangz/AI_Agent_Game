# Import libraries
from random_player import RandomPlayer

import sys
from Goal_player import GoalPlayer
from utility_player import UtilityPlayer
from min_max_player import Min_max_Player
from alpha_beta_player import AlphaBetaPlayer

from human_player import HumanPlayer

from game import Game
dict_player1={}
dict_player1[0]=HumanPlayer(1)
dict_player1[1]=GoalPlayer(1)
dict_player1[2]=UtilityPlayer(1)
dict_player1[3]=Min_max_Player(1)
dict_player1[4]=AlphaBetaPlayer(1)
dict_player2={}
dict_player2[0]=HumanPlayer(2)
dict_player2[1]=GoalPlayer(2)
dict_player2[2]=UtilityPlayer(2)
dict_player2[3]=Min_max_Player(2)
dict_player2[4]=AlphaBetaPlayer(2)
play1=HumanPlayer(1)

play2=AlphaBetaPlayer(2)
# Set the players for the game
# Note: Change these players to test different agents
player1 = play1
player2 = play2

# Loop until the user chooses to exit the program
while True:

    # Create a new game using the two players
    game = Game(player1, player2)

    # Play the game to it's conclusion
    game.play()
    
    # Ask the user if they want to continue
    choice = input("Play another game? Y/N: ")

    # Exit the program if the user doesn't want to play anymore
    if choice != "Y":
        break





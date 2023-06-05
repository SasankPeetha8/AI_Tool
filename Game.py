# Importing the player information
from PlayerInformation import Player
# Importing the Tic Tac Toe game
from BoardGames import TicTacToe
# Importing the MCTS
from AI import MCTS

# Importing the Game Environment
# from GameEnvironment import Environment
# # Importing the logging module
# import logging, json
# import math
from math import sqrt

###### Creating the Logger #########

# # Setting up logging file name
# log_filename = Environment.Logs_Filename
# # Setting the file mode
# log_filemode = 'w'
# # Setting the logging level
# log_level = logging.INFO
# # Creating a formatter
# log_formatter = "%(message)s"

# # Configuring the logger
# logging.basicConfig(filename=log_filename, filemode=log_filemode, encoding='utf-8', level=log_level, format=log_formatter)
# dic = { "Hello": "World", "Welcome 2": "Programming"}
# logging.info(json.dumps(dic, sort_keys=True, indent=4))


#####################################

### Defining the Global Variables ###

########### MCTS VALUES #############
MCTS_ITERATION_LIMIT = 1000
MCTS_TIME_LIMIT = 1
MCTS_EXP_CONST = sqrt(2)

######## ENVIRONMENT VALUES #########
BOARD_SIZE = 3
EMPTY_CHAR = "-"

############# lOG VALUES ############
LOGS_REQUIRED = True
LOGS_FILENAME = 'Game.json'

#####################################
######### Iteration Limit ###########
# Creating two players
# First Player
# First_Player = Player(character="X", type="mcts", iteration_limit=1000)
# # Second Player
# Second_Player = Player(character="O", type="mcts", iteration_limit=1000)

########## Time Limit ###############
# Creating two players
# First Player
First_Player = Player(character="X", type="mcts", time_limit=1)
# Second Player
Second_Player = Player(character="O", type="mcts", time_limit=1)
# Creating the game instance
Game = TicTacToe(board_size=BOARD_SIZE, char=EMPTY_CHAR,
                 first_player=First_Player, second_player=Second_Player)
# # Playing the game
Game.PlayGame()

# # Updating the player positions
# Game.BoardPositions = [ "X", "O", "-",
#                         "X", "-", "X",
#                         "O", "O", "-"]

# # Creating the MCTS
# # MCTS_Agent = MCTS(Game.BoardPositions, First_Player.Character, iteration_limit=10, time_limit=None, game_object=Game)
# MCTS_Agent = MCTS(game_object=Game)
# print(MCTS_Agent.BestMove())

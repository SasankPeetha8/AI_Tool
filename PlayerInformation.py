# Importing Game Environment Module
# from GameEnvironment import MCTS_Data
# Importing logging module
import logging
# Importing the os module
import os

# Importing the logger
# logger = logging.getLogger(__name__)

# Defining a class "PlayerInformation" which consists of mechanics to create a player that can be used in games
class Player():
    # Defining the lamda function
    __setTypeValue = lambda self, value : value.upper() if len(value) == 1 else value.lower()
    
    # Creating a object named player
    def __init__(self, character, type, iteration_limit=None, time_limit=None):
        # Defining the player character
        self.__Character = self.__setTypeValue(character[0])
        # Defining the player type
        self.__Type = self.__setTypeValue(type)
        # Defining the iteration limit  and time limit of the player
        # Defining the iteration limit  and time limit of the player if player type is mcts
        if self.__Type == "mcts":
            self.__IterationLimit, self.__TimeLimit = self.FetchLimits(iteration_limit, time_limit)
            self.__GameTree = None

        # self.logger = logging.getLogger(__name__)
        # self.logger.error("Created Player successfully")
        
    # Defining the property
    @property
    def Character(self):
        return self.__Character[:]
    
    @Character.setter
    def Character(self, value):
        self.__Character = self.__setTypeValue(value[0])
    
    @property
    def Type(self):
        return self.__Type[:]
    
    @Type.setter
    def Type(self, value):
        self.__Type = self.__setTypeValue(value)
    
    @property
    def IterationLimit(self):
        return self.__IterationLimit
    
    @property
    def TimeLimit(self):
        return self.__TimeLimit
    
    @property
    def GameTree(self):
        return self.__GameTree
    
    @GameTree.setter
    def GameTree(self, tree_data):
        self.__GameTree = tree_data
    
    # Defining method to find the limits
    def FetchLimits(self, iterations, time):
        # Checking if both iteration limit and time limit are empty
        if iterations or time:
            return iterations, time
        else:
            raise NoMCTSLimits
            os._exit()


# Defining class for raising exceptions
class NoMCTSLimits(Exception):
    """docstring for NoMCTSLimits."""
    def __init__(self):
        self.message = "No Limits are provided for the MCTS Player."
        super(NoMCTSLimits, self).__init__(self.message)
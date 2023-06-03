# Importing the random module
import random
# Importing the AI
from AI import MCTS
# Defining class for tic Tac toe game
class TicTacToe():
    """
    Defining the game mechanics for the tic tac toe board game
    """
    # Defining lambda function to fetch the required board positions
    __fetchBoardPositions = lambda self, value : value if value else self.BoardPositions
    # Defining Lambda function to find the positions
    __fetchAvailablePositions =  lambda self, value : [ each for each in range(len(value)) if value[each] == self.empty_char ]
    # Defining lambda function to extract unique elements
    __uniqueData = lambda self, list_data : list(set(list_data))
    # Defining lambda function to check if only one unique value is present
    __booleanValue = lambda self, list_data : list_data[0] if len(list_data)==1 else False
    # Extracting the list values horizontally
    __horizontalList = lambda self, list_data, size : [ list_data[each:each+size] for each in range(0, len(list_data), size) ]
    # Extracting the elements of the list vertically
    __verticalList = lambda self, list_data, size : [ list_data[each::size] for each in range(size) ]
    # Extracting the elements of the list in backward diagonal
    __backwardDiagoanlList = lambda self, list_data, board_size :  [ [ list_data[ (index*board_size)+index] for index in range(board_size) ] ]
    # Extracting the elements of the list in forward diagonal
    __forwardDiagonalList = lambda self, list_data, board_size: [ [ list_data[(board_size-1)*index] for index in range(1, board_size+1) ] ]
    
    # Defining method to initialize the class
    def __init__(self, first_player, second_player, board_size=3, char="-"):
        # Defining the board size
        self.__board_size = board_size
        # Defining the empty char
        self.__empty_char = char
        # Creating Board positions
        self.__BoardPositions = [ self.__empty_char ] * (self.__board_size * self.__board_size)
        # Creating the first player
        self.__FirstPlayer = first_player
        # Creating the second player
        self.__SecondPlayer = second_player
    
    # Defining the Properties i.e., getters and setters
    @property
    def board_size(self):
        return self.__board_size
    
    @property
    def empty_char(self):
        return self.__empty_char

    @property
    def BoardPositions(self):
        return self.__BoardPositions[:]
    
    @BoardPositions.setter
    def BoardPositions(self, positions):
        if len(self.__BoardPositions) == len(positions):
            self.__BoardPositions[:] = positions[:]
        else:
            ## NEEDS A LOG
            print("Invalid Board Positions Detected.")
            pass
    
    @property
    def FirstPlayer(self):
        return self.__FirstPlayer
    
    @property
    def SecondPlayer(self):
        return self.__SecondPlayer
    
    # Defining method to find the current player
    def FindCurrentPlayer(self, list_data=None):
        # Checking if the board position is passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Fetching the player count using lambda function
        FetchCount = lambda player : positions.count(player.Character)
        # Fetching the count difference
        count = FetchCount(self.FirstPlayer) - FetchCount(self.SecondPlayer)
        # Checking if the first player and second player are equal
        if count == 0:
            return self.FirstPlayer
        elif count == 1:
            return self.SecondPlayer
        else:
            return False
    
    # Defining method to fetch the available positions
    def AvailablePositions(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)    
        # Iterating through all the values in the list and returning the positions available
        return self.__fetchAvailablePositions(positions)
        
    # Defining method to fetch the available states
    def AvailableStates(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Fetching available positions
        available_positions = self.__fetchAvailablePositions(positions)
        # Fetching the current player character
        char = self.FindCurrentPlayer(positions).Character
        # Creating a lambda function
        updateElementValue = lambda list_data, value, letter: list_data[:value] + [letter] + list_data[value+1:]
        # Fetching the available states using the lambda functions
        available_states = [ updateElementValue(positions, each, char) for each in available_positions ]
        # Returning the available states
        return available_states
    
    # Defining method to check if the game is draw
    def IsDraw(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Checking if any positional values are available or not
        positions = self.__fetchAvailablePositions(positions)
        # Returning the length of the board positions
        return not bool(len(positions))
    
    # Defining method to check the list values
    def CheckListValues(self, list_data):
        # Extracting the unique data from the given list
        list_data = [ self.__uniqueData(each_list) for each_list in list_data ]
        # Extracting the boolean value of each list
        list_data = [ self.__booleanValue(each_list) for each_list in list_data]
        # Removing false from the list
        list_data = [ each for each in list_data if each not in [False, self.empty_char]]
        # Returning the values
        if len(list_data) == 1 :
            return list_data[0]
        elif len(list_data) == 0 :
            return False
        else:
            return "None"
    
    # Defining method to check if the game is won
    def IsWin(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Fetching the board size
        board_size = self.board_size
        # Checking all the elements and returning the boolean value
        return self.CheckListValues(self.__horizontalList(positions, board_size)) or \
                self.CheckListValues(self.__verticalList(positions, board_size)) or \
                self.CheckListValues(self.__backwardDiagoanlList(positions, board_size)) or \
                self.CheckListValues(self.__forwardDiagonalList(positions, board_size))
    
    # Displaying the board positions
    def __str__(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Fetching the board size
        board_size = self.board_size
        # Creating a string to display the positions of the game.
        game_positions = "\n"
        # Iterating through all the positions.
        for each_position in range(1, len(positions)+1):
            # Adding elements to the string appropriately.
            game_positions = game_positions + f" {positions[each_position-1]} " 
            game_positions = f"{game_positions}\n" if each_position % board_size == 0 else f"{game_positions}"
        # Returning the Positions of the Game.
        return game_positions
    
    # Defining method for the player input
    def PlayerInput(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Fetching the current player
        current_player = self.FindCurrentPlayer(positions).Character
        while True:
            # Displaying message asking user to input the position value
            position_value = input(f"Enter the position number [1-{len(positions)}]: ")
            # try to convert to integer
            try:
                position_value = int(position_value) - 1
            except ValueError:
                print("Invalid input provided. Please retry..")
                continue
            if position_value < len(positions) and positions[position_value] == self.empty_char:
                # Creating a temporary player position
                temp = positions[:]
                # updating the player position of the temp variable
                temp[position_value] = current_player
                return temp
            else:
                print("Invalid move is provided. Please retry..")

    
    # Defining method to play the game
    def PlayGame(self, list_data=None):
        # Checking if the board positions are passed or not
        positions = self.__fetchBoardPositions(list_data)
        # Iterating until all the positions are full
        for move in range(0, len(positions)+1):
            # Displaying the current game positions
            print(self.__str__(positions))
            
            winner = self.IsWin(positions)
            # Checking if the game is won
            if winner and winner != "None":
                print(f"The game is won by Player {winner}.")
                break
            # Checking if the game is draw
            elif self.IsDraw(positions):
                print(f"The game is draw.")
                break
            # IF not continue playing the game
            # Updating the curren player
            current_player = self.FindCurrentPlayer(positions)
            # Check if the current player is valid or not
            if current_player:
                # Printing which player should make the move
                print(f"Requesting '{current_player.Character}' to make the move - {move}")
                # Checking the type of the player
                if current_player.Type == "random":
                    # Extracting the available states
                    available_states = self.AvailableStates(positions)
                    # Making a random move
                    positions = random.choice(available_states) if len(available_states) > 1 else available_states[0]
                # Checking if the player type is Normal
                elif current_player.Type == "normal":
                    # Asking user to enter an input value
                    positions = self.PlayerInput(positions)
                else:
                    # Creating the MCTS AI Player
                    MCTS_Agent = MCTS(game_object=self)
                    # Checking if game tree is empty or not
                    if current_player.GameTree == None:
                        # Building the game tree
                        current_player.GameTree = MCTS_Agent.BuildTree()
                    else:
                        # Building Game Tree using the existing game tree
                        game_tree = MCTS_Agent.FindState(current_player.GameTree, positions)
                        print(f"The Found State: {game_tree}")
                        current_player.GameTree = MCTS_Agent.BuildTree(tree_data=game_tree)
                        
                    # Fetching the best move from the generated game tree
                    # Finding the best move using the AI
                    positions = MCTS_Agent.BestMove(current_player.GameTree)
                    # Updating the nodes as per the positions
                    current_player.GameTree = MCTS_Agent.FindState(current_player.GameTree, positions)
            # Invalid Moves are detected
            else:
                print(f"Invalid Moves Detected.")
                break
            # Updating the board positions
            self.BoardPositions = positions
            # Displaying the move count
            print(f" ---------- Move Count: {move + 1} ---------- ")
            # Defining the player turn
            print(f" ------------- Player Turn: {current_player.Character} ------------------")
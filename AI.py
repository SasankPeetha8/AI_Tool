# Importing the Game Tree Object
from GameTree import Tree
# Import time
import time
# Importing the math module
from math import sqrt, log10
# Importing the random module
import random, sys
# Importing deep copy 
from copy import deepcopy
# This file consists of all the items added together for the complete GUI Application
from PySide6.QtWidgets import QApplication, QMainWindow
from CustomizedCentralWidget import CentralWidget
from PySide6.QtGui import QScreen
from PySide6.QtCore import Qt
import random


# Creating class for defining the MCTS Algorithm
class MCTS():
    """
    This class is used to create the Monte Carlo Tree Search Algorithm
    """
    def __init__(self, game_object):
        # Copying the contents of the game object
        self.game_object = deepcopy(game_object)
        # Defining the board positions
        self.__PlayerPositions = self.game_object.BoardPositions
        # Defining the player character
        self.__Player = self.game_object.FindCurrentPlayer(self.__PlayerPositions)
        # Defining the iteration limit of the player
        self.__IterationLimit = self.__Player.IterationLimit
        # Defining the time limit of the player limit
        self.__TimeLimit = self.__Player.TimeLimit
        # Defining the exploration constant value
        self.__exp_const = sqrt(2)
        # self.__exp_const = 1/sqrt(2)
        
    
    # Defining the properites
    @property
    def PlayerPositions(self):
        return self.__PlayerPositions[:]
    
    @PlayerPositions.setter
    def PlayerPositions(self, list_data):
        self.__PlayerPositions = list_data[:]
    
    @property
    def IterationLimit(self):
        return self.__IterationLimit
    
    @property
    def ExpConst(self):
        return self.__exp_const
    
    @property
    def TimeLimit(self):
        return self.__TimeLimit
    
    # Defining method for score calculation
    def Calculate_Score(self, node_score, node_visits, parent_visits):
        # Calculating the exploitation value
        exploitation_value = node_score/node_visits
        # Calculating the exploration value
        exploration_value = self.ExpConst * ( sqrt((log10(parent_visits) )/node_visits ))
        # Calculating the total score
        score = exploitation_value + exploration_value
        # Returning the total score
        return round(score, 2)
    
    # Defining method for single node selection
    def Single_Select(self, node):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Single Select :::::::::: ")
        # Initialising list for best moves
        best_moves = [ ]
        # Initialising the best score
        best_score = float("-inf")
        # Calculating the score of each child node of the current node
        for index in range(0, len(node.ChildNodes)):
            # fetching the appropriate child node using index
            each_child = node.ChildNodes[index]
            # Calculating the score
            score = self.Calculate_Score(each_child.NodeScore, each_child.NodeVisits, node.NodeVisits)
            # Displaying the each node score and it's value
            print(f"Child Node - {index + 1} [{score}]:\n{each_child}")
            # Checking if the child node has the best score or not
            if score > best_score:
                # Appending the child node to list
                best_moves = [ each_child ]
                best_score = score
            elif score == best_score:
                # Appending the child node to the list
                best_moves = best_moves + [ each_child ]
        # Selecting the best move
        best_state = random.choice(best_moves) if (len(best_moves) > 1) else best_moves[0]
        # returning the best state
        print(f"The following node is selected in Single Select Phase:\n{best_state}")
        return best_state
            
    
    # Defining method for node selection
    def Select_Node(self, node):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Select Node :::::::::: ")
        # Checking if the node is a leaf node or not
        while True:
            if node.Is_Leafnode:
                print(f"The following node is selected in Select Node Phase:\n{node}")
                return node
            # If the node is not a leaf node then selecting the sub-child node
            else:
                node = self.Single_Select(node)
    
    # Defining the method for node expansion
    def Expand_Node(self, node):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Expand Node :::::::::: ")
        # Fetching the positions from the node state
        positions = node.NodeState
        # Checking if the node is win or draw
        if self.game_object.IsWin(positions) or self.game_object.IsDraw(positions):
            print(f"The selected node is terminal node.\n{node}")
            return node
        
        # Fetching all the possible states
        available_states = node.PossibleStates
        # # Selecting a random state
        # num = random.randint(0, len(available_states)-1)
        # # Selecting the appropriate state
        # selected_state = available_states[num]
        # # Updating the possible states of the node
        # node.PossibleStates = available_states[:num] + available_states[num+1:]
        # # Updating the node whether the node is leafnode or not
        # if len(node.PossibleStates) == 0:
        
        # Updating the leafnode status
        node.Is_Leafnode = False
            
        # Iterating through all the available states
        for index in range(len(available_states)):
            # Creating a new tree node
            new_node = Tree(current_state=available_states[index], possible_states=self.game_object.AvailableStates(available_states[index]), parent=node)
            # Updating the level of the child node
            new_node.treeDepth = node.treeDepth + 1
            # Appending the new node as child node
            node.ChildNodes = node.ChildNodes + [ new_node ]
            # Printing the node state
            print(f"Available States: {index+1}\n{new_node}")
            
        # # Creating a new tree node
        # new_node = Tree(current_state=selected_state, possible_states=self.game_object.AvailableStates(selected_state), parent=node)
        # # Updating the level of the child node
        # new_node.treeDepth = node.treeDepth + 1
        # # Appending the new node as child node
        # node.ChildNodes = node.ChildNodes + [ new_node ]
        # # Displaying the message
        # Choosing a child node at random
        selected_node = random.choice(node.ChildNodes) if len(node.ChildNodes) > 1 else node.ChildNodes[0]
        print(f"The following node is selected in the Expansion Phase:\n{selected_node}")
        # Returning the newly created child node
        return selected_node           
    
    # Defining method to simulate the nodes
    def Simulate_Node(self, node):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Simulate Node :::::::::: ")
        print(f"Initial Positions:\n{node}")
        # print(f" {'-'*20} ")
        # Fetching the positions in the node
        positions = node.NodeState
        # Fetching the current player character using the positions
        current_player = self.game_object.FindCurrentPlayer(positions).Character
        # Checking if the game is won or not
        while not (self.game_object.IsWin(positions) or self.game_object.IsDraw(positions)):
            # # Fetching all the possible states
            available_states = self.game_object.AvailableStates(positions)
            # Selecting a random state
            num = random.randint(0, len(available_states)-1)
            # Selecting the appropriate state
            positions = available_states[num]
            # Checking if the positions are not accurate
            if not bool(self.game_object.FindCurrentPlayer(positions)):
                print(f"Invalid Moves")
                break
            print(f"Generated States: [Initial Player: {current_player},  Player who made the move:{self.game_object.FindCurrentPlayer(positions).Character}]")
            print(f"______________________________________________________________________")
            print(f"{node.__str__(positions)}")
        # Checking if the game is won
        player = self.game_object.IsWin(positions)
        # Checking if the current player has won the game or not
        if bool(player) == True:
            score = 1 if current_player != player else -1
            print(f"Player {player} has won the game | Score: {score}")
        elif self.game_object.IsDraw(positions):
            score = 0.5
            print(f"The game is draw | Score: {score}")
        else:
            print("Simulation went wrong. Please check")
            exit()
        return score
        
    
    # Defining method to perform backpropogation
    def Backpropagate(self, score, node):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Backprogate :::::::::: ")
        # Creating the temporary score
        if score == 1:
            temp_score = -1
        elif score == -1:
            temp_score = 1
        else:
            temp_score = score
        # Iterating until root node is reached
        while True:
            # Updating the score of the node
            node.NodeScore = node.NodeScore + score
            # Swaping the node scores
            temp_score, score = score, temp_score
            # Updating the node visit count
            node.NodeVisits = node.NodeVisits + 1
            # Displaying the values
            print(f"Tree Path (B to T):\n{node}")
            print(f"Node Score: {node.NodeScore}, Node Visits: {node.NodeVisits}")
            print(f" -------------------- ")
            # Checking if the parent node is none or not
            if node.ParentNode != None:
                node = node.ParentNode
            else:
                break
        # Returning the node
        return node
    
    # Defining method to perfom iteration
    def Perform_Iteration(self, root_node, count):
        # Displaying message to show the current phase
        print(f" :::::::::: Inside Perform Rollout :::::::::: ")
        # Displaying message to view the Iteration limit
        print(f" ------ Iteration: {count} -------")
        
        # Defining the Phase 1 of MCTS
        node = self.Select_Node(root_node)
        
        # Defining the Phase 2 of MCTS
        node = self.Expand_Node(node)
        
        # Defining the Phase 3 of MCTS
        score = self.Simulate_Node(node)
        
        # Defining the Phase 4 of MCTS
        node = self.Backpropagate(score, node)
        
        # Retuning the node after performing iteration
        return node
    
    # Defining method to find best move using MCTS
    def BuildTree(self, tree_data = None):
        if tree_data == None:
            # Creating an empty node
            node = Tree(current_state=self.PlayerPositions, possible_states=self.game_object.AvailableStates(), parent=None)
        else:
            # Using the exisiting game tree
            node = tree_data
        # Displaying message to find the best move
        print(f" :::::::::: Inside Best Move :::::::::: ")
        # Checking iteration limit:
        if self.IterationLimit:
            # looping through all the iterations
            for count in range(1, self.IterationLimit + 1):
                # Performing iteration
                node = self.Perform_Iteration(node, count)
        else:
            total_time = time.time() + self.TimeLimit
            # Specifying the count
            count = 1
            # Looping until the current time limit doesn't exceed the total time limit
            while time.time() < total_time:
                # Performing a rollout until the time limit has reached
                node = self.Perform_Iteration(node, count)
                # Updating the count value
                count = count + 1
        # Displaying the total iteration count
        print(f" ========== Total Iteration Count: {count} ========== ")
        print(f"_______________Visualizing the Node_________________\ngraph TD\n")
        print(f"{node.Visualise_Tree(node)}")
        print(f"____________________________________________________")
        print(f"________________Tree Flatten_________________________")
        # node.FlattenTreeDataStructure(node)
        # print(f"{node.treeStructure}")
        # node.FlattenNodes(node)
        print(f"________________Tree Flatten_________________________")
        # self.ViewGUI(node)
        return node
    
    # Defining method to find the current game state:
    def FindState(self, tree_data, positions):
        # Iterating through all the nodes in the game tree
        for each_node in tree_data.ChildNodes:
            # Checking if the state of the child node is found
            if each_node.NodeState == positions:
                # Removing the parent of the child node
                each_node.ParentNode = None
                # Displaying the message
                print(f"State found: {each_node.NodeState} == {positions}")
                # Returning the child node
                return each_node
    
    # Defining method to find best move using MCTS
    def BestMove(self, node):
        # Fetching the best node
        best_move = self.Single_Select(node)
        # Displaying the message
        print(f"The following node is selected in the Best Move:\n{best_move}")
        # Printing the seperator line
        print(f"{'*'*30}")
        # Returning the positions of the best node
        return best_move.NodeState
    
    # Defining method to view the GUI
    def ViewGUI(self, treenode):
        # Checking if the previous instance exists or not
        if not QApplication.instance():
            application = QApplication(sys.argv)
        else:
            application = QApplication.instance()
        # Creating an instance of the GUI Application
        # application = QApplication()
        # Fetching the application properties
        SCREEN_SIZE = QScreen.availableGeometry(QApplication.primaryScreen()).getRect()
        # Specifying the screen size
        SCREEN_WIDTH = SCREEN_SIZE[2]
        SCREEN_HEIGHT = SCREEN_SIZE[3]
        # Specifying the application size
        APPLICATION_WIDTH = SCREEN_WIDTH//1.5
        APPLIATION_HEIGHT = SCREEN_HEIGHT//1.5
        
        # Specifying the main window
        main_window = QMainWindow()
        # Specifying the size of the main window
        # main_window.resize(1280, 720)
        main_window.resize(SCREEN_WIDTH, SCREEN_HEIGHT-50)
        main_window.setWindowState(Qt.WindowMaximized)
        # print(f"Geometry: {main_window.frameSize()}")
        # main_window.isMaximized()
        # main_window.resized

        # Creating an instance of the central widget
        tree_view = CentralWidget(main_window, SCREEN_WIDTH, SCREEN_HEIGHT)
        # Adding the tree nodes to the structure
        # Fetching the treeStructure
        # tree_structure = deepcopy(treenode.treeStructure)
        # Flattenning the nodes
        tree_nodes = deepcopy(treenode.treeNodes)
        # Iterating through all the items in the dictionary
        for each_key in tree_nodes.keys():
            # Extracting the contents of the list
            list_data = tree_nodes[each_key][:]
            # Fetching the maximum count inside the list
            # max_elements = self.FindMaxCount(list_data)
            max_elements = len(list_data)
            # Adding the nodes to the central widget
            tree_view.addTreeNodes(list_data, max_elements)
            
        # Displaying the nodes
        tree_view.DisplayNodes()
        # Displaying the lines
        tree_view.ViewLines()
        # Specifying the central widget
        main_window.setCentralWidget(tree_view.drawLabel)
        # Displaying the main window
        main_window.show()
        # Running the application
        application.exec()
        
    # Defining method to extract the max count inside the list
    def FindMaxCount(self, list_data):
        # Initialising the max count as zero
        max_count = 0
        # Iterating through all the elements in the list
        for each_list in list_data:
            # Finding the max count of the list
            max_count = len(each_list) if len(each_list) >= max_count else max_count
            
        # Returning the max count values
        return max_count*len(list_data)
    
    # Defining method to add visualization functionality
    def VisualizeGraphStructure(self, node):
        # Iterating through all the available child nodes
        pass
    
    
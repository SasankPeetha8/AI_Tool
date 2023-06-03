# Importing the math module
from math import sqrt, log10
from copy import deepcopy
# Defining the class for the game tree
class Tree():
    """Defining the class for the game tree"""
    def __init__(self, current_state, possible_states, parent=None ):
        # Defining the parent node
        self.__ParentNode = parent
        # Defining the current state of the node
        self.__NodeState = current_state
        # Defining the child nodes
        self.__ChildNodes = []
        # Defining the Node visits
        self.__NodeVisits = 1
        # Defining the node score
        self.__NodeScore = 0
        # Defining boolean value to check if the node is a leaf node
        self.__Is_Leafnode = True
        # Defining list to store all the possible states
        self.__PossibleStates = possible_states
        # Defining the total
        self.__Total = 0
        # Defining the tree depth
        self.__treeDepth = 0
        # Defining tree flatten
        self.treeStructure = { }
        # Defining the tree nodes
        self.treeNodes = { }
        
    # Defining the properties
    @property
    def ParentNode(self):
        return self.__ParentNode
    
    @ParentNode.setter
    def ParentNode(self, val):
        self.__ParentNode = val
    
    @property
    def ChildNodes(self):
        return self.__ChildNodes[:]
    
    @ChildNodes.setter
    def ChildNodes(self, list_data):
        # Checking if the length is equal or not
        self.__ChildNodes = list_data[:]
    
    @property
    def NodeState(self):
        return self.__NodeState[:]
    
    @NodeState.setter
    def NodeState(self, list_data):
        # Checking if the length is equal or not
        if len(self.NodeState) == len(list_data):
            self.__NodeState = list_data[:]
        else:
            raise Exception("Invalid Node State")
        
    @property
    def NodeVisits(self):
        return self.__NodeVisits
    
    @NodeVisits.setter
    def NodeVisits(self, value):
        self.__NodeVisits = value
        
    @property
    def NodeScore(self):
        return self.__NodeScore
    
    @NodeScore.setter
    def NodeScore(self, value):
        self.__NodeScore = value
        
    @property
    def Is_Leafnode(self):
        return self.__Is_Leafnode
    
    @Is_Leafnode.setter
    def Is_Leafnode(self, value):
        # if type(value) == "bool":
        #     self.__Is_Leafnode = value
        # else:
        #     raise Exception("Invalid boolean for Is_Leafnode")
        self.__Is_Leafnode = value
        
    @property
    def treeDepth(self):
        return self.__treeDepth
    
    @treeDepth.setter
    def treeDepth(self, val):
        self.__treeDepth = self.__treeDepth + int(val)

    @property
    def PossibleStates(self):
        return self.__PossibleStates[:]
    
    @PossibleStates.setter
    def PossibleStates(self, list_data):
        self.__PossibleStates[:] = list_data[:]
        
    # Defining the method to display the board.
    def __str__(self, list_data=None):
        """
        Summary:
        --------
        This method is used to display the current board positions.
        Returns:
        --------
        game_positions : str
            It returns the current board positions in the form of a string.
        """
        # Fetching the board positions
        positions = self.NodeState if list_data == None else list_data
        # Creating a string to display the positions of the game.
        game_positions = "\n"
        # Fetching the board size
        board_size = sqrt(len(positions))
        # Converting the board size to integer
        board_size = int(board_size)
        # Iterating through all the positions.
        for each_position in range(1, len(positions)+1):
            # Adding elements to the string appropriately.
            game_positions = game_positions + f" {positions[each_position-1]} " 
            game_positions = f"{game_positions}\n" if each_position % board_size == 0 else f"{game_positions}"
        # Returning the Positions of the Game.
        return game_positions

     # Defining method to visualize the tree.    
    def Visualise_Tree(self, tree_node):
        # Defining Empty Message
        message = ""
        # Initialising the Tree Node
        parent_index = f"{id(tree_node)}"
        # Removing the un-necessary text values
        # parent_index = parent_index.replace("<TreeNode.TreeNode object at ", "")
        # parent_index = parent_index.replace(">","")
        # Fetching child nodes
        children_nodes = tree_node.ChildNodes[:]
        # Checking if the tree_node has more than one child node
        if len(children_nodes) > 0 :
            # Iterating along all the child nodes
            for each_child in children_nodes:
                # Checking if the each child node count is zero or not
                if each_child.NodeVisits == 0:
                    exploitation_value = 0
                    exploration_value = 0
                else:
                    # Node Visits = 1 only when node_visits is zero
                    exploitation_value = each_child.NodeScore/each_child.NodeVisits
                    exploration_value = sqrt((2 * log10(tree_node.NodeVisits))/each_child.NodeVisits)
                
                # Calculating the total score using exploration value and exploitation value
                score = exploitation_value + exploration_value
                # Rounding the score value
                score = round(score, 3)
                # Updating the score of each child
                each_child.__Total = score
                # parent_total = 0 if tree_node.NodeVisits == 0 else tree_node.NodeScore/tree_node.NodeVisits
                # child_total = 0 if each_child.NodeVisits == 0 else ( each_child.NodeScore / each_child.NodeVisits ) + each_child.NodeText
                # Creating the parent string
                parent_str = f"{parent_index}[Score = {tree_node.NodeScore}\nVisits = {tree_node.NodeVisits}\nT = {tree_node.__Total}\nDepth: {tree_node.treeDepth}\n{tree_node.__str__(tree_node.NodeState)}]".replace("\n","<br/>")
                # Creating the child index string
                child_index = f"{id(each_child)}"
                # Removing the un-necessary text values
                child_index = child_index.replace("<TreeNode.TreeNode object at ", "")
                child_index = child_index.replace(">","")
                # Creating the child string
                child_str = f"[Score = {each_child.NodeScore}\nVisits = {each_child.NodeVisits}\nT = {each_child.__Total}\nDepth: {each_child.treeDepth}\n\n{each_child.__str__(each_child.NodeState)}]".replace("\n","<br/>")
                # Displaying the entire string
                message = message + f"    {parent_str} --> {child_index}{child_str}"
                # Iteratively Calling Visualise_Tree method
                message = message + "\n" + self.Visualise_Tree(each_child)
        # Returning the message found
        return message
    
    # # Defining method to iterate through the tree data structure
    # def IterateTree(self, treenode):
    #     # Fetching the child nodes available
    #     children_nodes = treenode.ChildNodes[:]
    #     # Iterating through all the child nodes
    #     for each_child in children_nodes:
            
    
    # Defining method to flatten the tree data structure
    # def FlattenTreeDataStructure(self, treenode, dict_data=None):
    def FlattenTreeDataStructure(self, treenode):
        # if dict_data:
        #     tree_structure = dict_data
        # else:
        #     # Initialising empty dictionary
        #     tree_structure = {}
        # tree_structure = {}
        # Iterating through all the elements of the treenode
        # Fetching the child nodes available
        if treenode.treeDepth in self.treeStructure.keys():
            if treenode.NodeState in self.treeStructure[treenode.treeDepth]:
                pass
            else:
                self.treeStructure[treenode.treeDepth] = self.treeStructure[treenode.treeDepth][:] + [ treenode.NodeState ]
        else:
            self.treeStructure[treenode.treeDepth] = [ treenode.NodeState ]
        # Fetching the available child nodes
        children_nodes = treenode.ChildNodes[:]
        # Iterating through all the child nodes
        for each_child in children_nodes:
            # Checking if the existing key is available in the dictionary
            if each_child.treeDepth in self.treeStructure.keys():
                # Checking if the existing state is present or not
                if each_child.NodeState in self.treeStructure[each_child.treeDepth]:
                    pass
                else:
                    # Appending the node state to the dictionary at particualr depth
                    self.treeStructure[each_child.treeDepth] = self.treeStructure[each_child.treeDepth][:] + [ each_child.NodeState ]
            else:
                self.treeStructure[each_child.treeDepth] = [ each_child.NodeState ]
            # Continuing with next iteration
            self.FlattenTreeDataStructure(each_child)
        # Returning the tree structure
        # return tree_structure
    
    # Defining method to find the available states
    def FindAvailableStates(self, list_data):
        # Initialising the available states
        available_states = [ ]
        # Iterating through all the available states in the list
        for each_node in list_data:
            # Adding each state to the list if not available
            if each_node.NodeState not in available_states:
                # Appending the state to the list
                available_states = available_states + [ each_node.NodeState ]
        # Returning the states available
        return available_states[:]
    
    # Defining method to flatten the node trees
    def FlattenNodes(self, treenode):
        # print(f"Inside the Flatten Node Method")
        # # Extracting the node i.e., root node
        # print(f"Current Node State: {treenode.NodeState}, and it's Depth is {treenode.treeDepth}")
        if treenode.treeDepth in self.treeNodes.keys():
            # extract the states at the current key depth
            states_available = self.FindAvailableStates(self.treeNodes[treenode.treeDepth])
            # Checking the current node state is available or not
            if treenode.NodeState in states_available:
                pass
            else:
                self.treeNodes[treenode.treeDepth] = self.treeNodes[treenode.treeDepth][:] + [ treenode ]
        # If the tree depth key isn't available in the self tree ndoes
        else:
            self.treeNodes[treenode.treeDepth] = [ treenode ]
        
        states_available = [ ]
        # Extracting the child nodes
        children_nodes = treenode.ChildNodes[:]
        # Iterating through all the child nodes
        for each_child in children_nodes:
            # Checking if the existing key is available in the dictionary
            if each_child.treeDepth in self.treeNodes.keys():
                # Extracting all the states available at the particular state
                states_available = self.FindAvailableStates(self.treeNodes[each_child.treeDepth])
                # Checking if the exisiting state is present or not
                if each_child.NodeState in states_available:
                    pass
                else:
                    # Appending the node state to the dictionary at particular depth
                    self.treeNodes[each_child.treeDepth] = self.treeNodes[each_child.treeDepth][:] + [ each_child ]
                
            else:
                # Appending the new key to the tree nodes dictionary
                self.treeNodes[each_child.treeDepth] = [ each_child ]
            # Continuning with next iteration
            self.FlattenNodes(each_child)
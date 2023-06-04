# Importing the required modules
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QVBoxLayout, QGraphicsLineItem
from PySide6.QtGui import QPen, QBrush, QColor, QPainterPath, QPainter

# Importing the required mathematical functions from math module
from math import sin, cos, radians, sqrt
# Importing the required circular button
from CircularButtonWidget import CircularButton

# Creating a class which inherits QWidget
class CustomCentralWidget(QWidget):
    """docstring for CircularButton."""
    def __init__(self):
        super(CustomCentralWidget, self).__init__()
        # Creating a graphic scene
        self.graphics_scene = QGraphicsScene()
        # Creating a graphics view
        self.graphics_view = QGraphicsView(self.graphics_scene)
        # Making the rendering output smooth
        self.graphics_view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        
        # Defining the pen
        self.pen = QPen(QColor(190, 189, 191))
        # Defining the width of the pen
        self.pen.setWidth(1)
        
        # # Creating a line
        # self.line = QGraphicsLineItem(0,0, 100, 100)
        # # Specifying the pen for the line
        # self.line.setPen(self.pen)
        # # Adding the line to the graphics scene
        # self.graphics_scene.addItem(self.line)

        
        # Specifying the vertical layout for the widget
        layout = QVBoxLayout(self)
        # Adding graphics view to the layout
        layout.addWidget(self.graphics_view)
        # Specifying the layout of the widget
        self.setLayout(layout)
        
        # Defining the angle
        self.__totalAngle = 360
        # Defining the radius
        self.__radius = 20
        # Defining the available circular buttons
        self.__availableButtons = [ ]
        # Defining the width of the graphics view
        self.__width = 1
        # Defining the height of the graphics view
        self.__height = 1
        
        # Defining the radius multiplier
        self.__radiusMultiplier = 0
        # Defining the level of circles
        self.__circleLevels = 0
        
        # Available Node Data
        self.__availableNodeData = { }

    # Defining method to check for overlapping
    def __OverLap(self, obj_1, obj_2):
        # Calculating the distance between two circles
        distance = sqrt((obj_1[0]-obj_2[0])**2 + (obj_1[1]-obj_2[1])**2)
        # Returning the boolean value
        return True if distance < self.__radius+3 else False

    # Defining method to calculate the positions
    def CalculatePositions(self, circles_required):
        # Initialising the emtpy list to store the values
        positions = []
        # Calculating the angle for each value
        angle_required = self.__totalAngle / circles_required
        # Calculating the distance from the center based on the angle
        distance = (self.__radius * self.__radiusMultiplier) + \
            (self.__circleLevels * (self.__radius/3))
        # Initialising the center
        x_centre = 0
        y_centre = 0
        # Iterating through all the elements
        for each in range(circles_required):
            # Calculating the x-coordinate
            x_position = x_centre + \
                ((distance) * sin(radians(angle_required * each)))
            # Calculating the y-coordinate
            y_position = y_centre + \
                ((distance) * cos(radians(angle_required * each)))
            # Adding the positional values to the list
            positions = positions + [(x_position, y_position)]
            
            # Checking if the length of the positions is 2
            if len(positions) == 2:
                # Checking if the co-ordinates are overlapping or not
                if self.__OverLap(obj_1=positions[-2], obj_2=positions[-1]):
                    # If overlapping, then calculating the values from the beginning
                    self.__radiusMultiplier = self.__radiusMultiplier + 1
                    # Returning the values
                    return self.CalculatePositions(circles_required)
        
        # Returning the calculated the positional values
        # distance_value = (self.__radius * self.__radiusMultiplier) + (self.__circleLevels)
        distance_value = (self.__radius * self.__radiusMultiplier) + (self.__circleLevels * (self.__radius/3))
        distance_value = distance_value + distance_value
        
        # Before returning the original positions, setting the default multiplier to 0
        self.__radiusMultiplier += 1
        
        # circle = QGraphicsEllipseItem(0-distance + 10, 0-distance + 10, distance_value, distance_value)
        circle = QGraphicsEllipseItem(0-distance + self.__radius/2, 0-distance + self.__radius/2, distance_value, distance_value)
        
        circle.setPen(self.pen)
        self.graphics_scene.addItem(circle)
        return positions
    
    # Defining method to add nodes to the frame
    def addNodes(self, list_data, totalNodes):
        # Initalising the following parameters
        # Maximum width
        maximum_x = 0
        # Maximum height
        maximum_y = 0
        # Fetching the co-ordinates available
        node_positions = self.CalculatePositions(totalNodes)
        # Iterating through all the nodes
        for each_node in range(len(node_positions)):
            x_value, y_value = node_positions[each_node][0], node_positions[each_node][1]
            # Creating a button and adding it into the frame
            self.__availableButtons = self.__availableButtons + \
                [CircularButton(x_pos=x_value, y_pos=y_value,
                                size=self.__radius, node_data=list_data[each_node])]
                
            # Fetching the node information
            self.__availableNodeData[f"{id(list_data[each_node])}"] = ( x_value, y_value )
            
            maximum_x = abs(x_value) if maximum_x < abs(x_value) else maximum_x
            maximum_y = abs(y_value) if maximum_y < abs(y_value) else maximum_y
            
            print(f"Node: {x_value}, {y_value}")
            
        # Updating the circle levels for the another layers
        self.__circleLevels = self.__circleLevels + 1
        # Finding the maximum value
        # self.__resizeTreeFrame(maximum_x + (self.__radius*2), maximum_y + (self.__radius*2))
        
    # Defining method to resize the widget
    def __resizeTreeFrame(self, width, height):
        # Updating the frame width
        print(f"Frame Details: {width}, {height}")
        if self.__width < (width*2):
            self.__width = width * 2
        if self.__height < (height*2):
            self.__height = height * 2
        
        # self.treeFrame.setGeometry(0, 0, self.__width, self.__height)
        self.graphics_view.setFixedSize(self.__width, self.__height)
        print(f"Graphics View Frame Size: {self.__width}, {self.__height}")
    
    # Defining method to display the lines
    def DisplayLines(self):
        # Iterating through all the nodes available
        for each_button in self.__availableButtons:
            # Extracting the node information
            node_info = each_button.node_info
            # Fetching the parent node of the current node
            parent_node = node_info.ParentNode
            # Checking if parent is none or not
            if parent_node == None:
                continue
            # Fetching the co-ordinates of the parent node
            values = self.__availableNodeData[f"{id(parent_node)}"]
            # Drawing line
            drawLine = QGraphicsLineItem(values[0]+self.__radius/2, values[1], each_button.xPosition, each_button.yPosition)
            # Adding the button to the graphics view
            self.graphics_scene.addItem(drawLine)
        
    # Defining method to display the nodes
    def DisplayNodes(self):
        # Iterating through all the nodes available
        for each_button in self.__availableButtons:
            # Adding the button to the graphics view
            self.graphics_scene.addItem(each_button)
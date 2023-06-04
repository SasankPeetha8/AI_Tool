# Importing the required modules
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtGui import QPen, QBrush
from PySide6.QtCore import Qt

# Creating a class which inherits the Ellipse Item
class CircularButton(QGraphicsEllipseItem):
    """docstring for CircularButton."""
    def __init__(self, x_pos, y_pos, size, node_data):
        # Returning a Ellipse Item with given X and Y co-ordinates followed by width and height
        super(CircularButton, self).__init__(x_pos, y_pos, size, size)
        
        # Defining the positions
        self.xPosition = x_pos
        self.yPosition = y_pos
        self.size = size
        
        # Defining the node info
        self.node_info = node_data
        
        # Creating a new pen
        self.__pen = QPen(Qt.black)
        # Creating a new brush
        self.__brush = QBrush(Qt.blue)
        
        # Specifying to use the pen
        self.setPen(self.__pen)
        # Specifying to use the brush
        self.setBrush(self.__brush)
        
        # Accepting the events
        self.setAcceptHoverEvents(True)
    
    # Defining the mouse press event
    def mousePressEvent(self, event):
        # Checking if the mouse press event is left mouse button
        if event.button() == Qt.LeftButton:
            # Specifying the colour of the brush
            self.__brush = QBrush(Qt.black)
            # Specifying to use the brush
            self.setBrush(self.__brush)
            print(f"Mouse Left Button is pressed")
            
    # Defining the mouse release event
    def mouseReleaseEvent(self, event):
        # Checking if the mouse release event is left mouse button
        if event.button() == Qt.LeftButton:
            # Specifying the colour of the brush
            self.__brush = QBrush(Qt.blue)
            # Specifying to use the brush
            self.setBrush(self.__brush)
            print(f"Mouse Left Button is released")
            print(f"{self.node_info}")
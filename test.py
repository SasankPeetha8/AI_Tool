import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
# from networkx import graphviz_layout
from networkx.drawing.nx_agraph import graphviz_layout

# try:
#     from networkx import graphviz_layout
# except ImportError:
#     raise ImportError("This example needs Graphviz and either PyGraphviz or Pydot")


G = nx.balanced_tree(3, 5)
pos = graphviz_layout(G, prog='twopi', args='')
plt.figure(figsize=(8, 8))

# Draw nodes
nodes = nx.draw_networkx_nodes(G, pos, node_size=20, alpha=0.5, node_color="blue")

# Customize the drawing of nodes as buttons
ax = plt.gca()  # Get the current axes instance
buttons = []
for node, (x, y) in pos.items():
    # Create a clickable button
    # button = Button(ax, (x, y), 0.02, 0.02, label=str(node), color='red')
    # from matplotlib.widgets import Button

    # let's say ax is your axes
    button = Button(ax, label='Button Label')


    def on_button_click(event):
        print("Button", event)
        # Define the action you want to perform when the button is clicked

    # Attach the click event handler to the button
    button.on_clicked(on_button_click)
    buttons.append(button)

# Draw edges
nx.draw_networkx_edges(G, pos)

plt.axis('equal')
plt.savefig('circular_tree.png')
plt.show()

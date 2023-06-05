import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# Create a new directed graph
G = nx.DiGraph()

# Add some nodes to the graph
G.add_edge("a", "b")
G.add_edge("a", "c")
G.add_edge("b", "d")
G.add_edge("b", "e")
G.add_edge("c", "f")
G.add_edge("c", "g")
G.add_edge("d", "h")

# Create the layout for the nodes
pos = graphviz_layout(G, prog='twopi', args='', root='a')


# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, pos, node_size=60, alpha=0.5, node_color="blue", with_labels=False)
plt.axis('equal')
plt.show()

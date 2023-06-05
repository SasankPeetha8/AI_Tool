from pyvis.network import Network
import networkx as nx
import webbrowser
import pygraphviz as pgv

# Create the network graph
graph = Network()
graph.add_node(1, label='Node 1')
graph.add_node(2, label='Node 2')
graph.add_node(3, label='Node 3')
graph.add_node(4, label='Node 4')
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

# Convert the graph to a tree structure
G = nx.Graph()


# Extract nodes and edges from the Pyvis graph
nodes = [node['id'] for node in graph.nodes]
edges = [(edge['from'], edge['to']) for edge in graph.edges]

# Add nodes and edges to the networkx graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Create a radial tree structure
root = 1  # Define the root node of the tree
pos = nx.nx_agraph.graphviz_layout(G, prog='twopi', root=root)

# Create a new Pyvis graph
graph = Network()

# Add nodes to the graph with positions
for node in G.nodes:
    x, y = pos[node]
    graph.add_node(node, label=f'Node {node}', x=x * 100, y=y * 100)

# Add edges to the graph
for edge in G.edges:
    src, dst = edge
    graph.add_edge(src, dst)


# Display the graph
graph.write_html('graph.html')


webbrowser.open('graph.html')

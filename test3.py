from pyvis.network import Network
from IPython.display import display

graph = Network(notebook=True)

graph.add_node(1, label='Node 1')
graph.add_node(2, label='Node 2')
graph.add_node(3, label='Node 3')

graph.add_edge(1, 2, arrows="to")
graph.add_edge(2, 3, arrows="to")
graph.add_edge(3, 1, arrows="to")

# display(graph.show('graph.html'))
graph.force_atlas_2based()
graph.show_buttons(embedded=True)
display(graph.show('graph.html', notebook=False))

# from pyvis.network import Network
# import networkx as nx
# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10
# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# nt = Network('500px', '500px')
# # populates the nodes and edges data structures
# nt.from_nx(nx_graph)
# nt.show('nx.html', notebook=False)
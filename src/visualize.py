import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, partition):
    pos = nx.spring_layout(G, k=0.15)
    colors = [partition.get(node, 0) for node in G.nodes()]
    nx.draw(G, pos, node_color=colors, node_size=50, with_labels=False)
    plt.show()

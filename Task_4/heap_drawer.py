import matplotlib.pyplot as plt
import networkx as nx
from heap_builder import build_heap_tree, add_heap_edges


def draw_heap(arr):
    nodes = build_heap_tree(arr)
    if not nodes:
        print("Empty heap")
        return

    graph = nx.DiGraph()
    pos = {nodes[0].id: (0, 0)}
    graph = add_heap_edges(graph, nodes, pos)

    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_size=12)
    plt.show()

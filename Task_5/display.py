import networkx as nx
import matplotlib.pyplot as plt
from utils import add_edges, generate_colors

def display_traversal(root, traversal_func, title="Traversal"):
    order = traversal_func(root)
    colors = generate_colors(len(order))

    for i, node in enumerate(order):
        node.color = colors[i]

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    node_colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(8, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors, font_size=12)
    plt.title(title)
    plt.show()

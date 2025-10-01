import networkx as nx
from heap_node import HeapNode


def build_heap_tree(arr):
    return [HeapNode(val) for val in arr]


def add_heap_edges(graph, nodes, pos, i=0, x=0, y=0, layer=1):
    if i < len(nodes):
        graph.add_node(nodes[i].id, color=nodes[i].color, label=nodes[i].val)
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            graph.add_edge(nodes[i].id, nodes[left].id)
            lx = x - 1 / 2 ** layer
            pos[nodes[left].id] = (lx, y - 1)
            add_heap_edges(graph, nodes, pos, left, lx, y - 1, layer + 1)

        if right < len(nodes):
            graph.add_edge(nodes[i].id, nodes[right].id)
            rx = x + 1 / 2 ** layer
            pos[nodes[right].id] = (rx, y - 1)
            add_heap_edges(graph, nodes, pos, right, rx, y - 1, layer + 1)

    return graph

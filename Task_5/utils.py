def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_colors(n, base_color=(132, 0, 71)):
    colors = []
    step = 200 // (n + 1)
    for i in range(n):
        r = min(255, base_color[0] + i * step)
        g = min(255, base_color[1] + i * step)
        b = min(255, base_color[2] + i * step)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

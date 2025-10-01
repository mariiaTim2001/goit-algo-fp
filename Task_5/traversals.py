from collections import deque

def bfs_traversal(root):
    order = []
    queue = deque([root])
    visited = set()
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order


def dfs_traversal(root):
    order = []
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order

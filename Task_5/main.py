from node import Node
from traversals import bfs_traversal, dfs_traversal
from display import display_traversal

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.left.right.left = Node(2)
    root.left.right.right = Node(8)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(6)
    root.right.right.left = Node(7)

    display_traversal(root, bfs_traversal, title="Breadth-First Search (BFS)")
    display_traversal(root, dfs_traversal, title="Depth-First Search (DFS)")

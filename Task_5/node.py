import uuid

class Node:
    def __init__(self, key, color="#840047"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" -> ".join(result) if result else "Empty List")

# Node class to represent each node in the circular list
class Node:
    def __init__(self, data):
        self.data = data  # Stores the value of each node
        self.next = None  # Pointer to the next node

# CircularList class to manage a circular linked list
class CircularList:
    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list pointing to the first

    # Adds a new node to the end of the list
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, the node becomes both head and tail
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circularity
        else:
            # If the list has elements, add the node to the end
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circularity

    # Returns the first node of the list
    def get_head(self):
        return self.head

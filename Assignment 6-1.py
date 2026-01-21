from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head:
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Assignment 6-1: Recursive Reverse
def reverse_recursive(self, node):
    # Base case: if list is empty pr reaching the last node
    if not node or not node.next:
        return node

    # Reverse the rest of the list
    new_head = self.reverse_recursive(node.next)

    # Make the next node point back to the current node
    node.next.next = node
    node.next = None

    return new_head
def reverse(self):
    self.head = self.reverse_recursive(self.head)

# Test Assignment 6-1
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
print("Original List:")
llist.print_list()

llist.reverse()
print("Reversed List:")
llist.print_list()



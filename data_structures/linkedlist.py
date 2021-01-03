class Node(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    """ Implementation of double linked list """
    def __init__(self):
        self.head = None

    def search(self, k):
        """ Find a node with key k """
        node = self.head
        while node is not None and node.key != k:
            node = node.next
        return node

    def insert(self, k):
        """ Insert a node with key k at the head of the list """
        node = Node(k)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def delete(self, k):
        """ Delete a node with key k """
        node = self.search(k)
        if node is not None:
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
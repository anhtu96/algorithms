class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """ Checks if queue is empty """
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, key):
        """ Add new key into the queue's tail """
        node = Node(key)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def dequeue(self):
        """ Remove queue's head """
        if not self.is_empty():
            value = self.head.key
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return value
            
    def peak(self):
        """ Return head value """
        if not self.is_empty():
            return self.head.key
class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None

    def is_empty(self):
        """ Check whether the stack is empty. """
        if self.top is None:
            return True
        else:
            return False

    def push(self, key):
        """ Add new key to the top of the stack. """
        new_node = Node(key)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """ Remove and return the stack's top key (LIFO). """
        if not self.is_empty():
            pop_value = self.top.key
            self.top = self.top.next
        else:
            pop_value = None
        return pop_value

    def peak(self):
        """ Return the stack's top key. """
        if not self.is_empty():
            return self.top.key
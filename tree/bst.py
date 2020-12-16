class BSTNode(object):
    """A node in a BST tree."""
    def __init__(self, parent, k):
        """
        Create a node.
        Args:
            parent: node's parent.
            k: key of the node.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """
        Find and returns the node with key k from the subtree rooted at this node.
        Args:
            k: key of the node we want to find.
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        """
        Finds the node with minimum key in the subtree rooted at this node.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        """
        Finds the node with next larger key (the successor) in the BST.
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """
        Inserts a node into the subtree rooted at this node.
        Args:
            node: the node to be inserted.
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is not None:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right is not None:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node

    def delete(self):
        """
        Deletes and returns this node.
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()
    
class BST(object):
    def __init__(self):
        self.root = None

    def find(self, k):
        """
        Finds the node with key k.
        Args:
            k: key of the node we want to find.
        """
        return self.root and self.root.find(k)

    def find_min(self):
        """
        Finds the node with minimum key.
        """
        return self.root and self.root.find_min()

    def insert(self, k):
        """
        Inserts a node with key k into the BST.
        Args:
            k: key of the node we want to insert.
        """
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def delete(self, k):
        """
        Deletes a node with key k.
        Args:
            k: key of the node.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = BSTNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()
    
    def next_larger(self, k):
        """
        Finds the node that contains the next larger key
        in the BST in relation to the node with key k.
        Args:
            k: the key of the node of which the successor is to be found.
        Returns:
            The successor node.
        """
        node = self.find(k)
        return node and node.next_larger()
    

class MinBSTNode(BSTNode):
    """
    A node in BST which is augmented to keep track of the node with the
    minimum key in the subtree rooted at this node.
    """
    def __init__(self, parent, key):
        super(MinBSTNode, self).__init__(parent, key)
        self.min = self


def inorder_traverse(node):
    if node is not None:
        inorder_traverse(node.left)
        print(node.key)
        inorder_traverse(node.right)

def preorder_traverse(node):
    if node is not None:
        print(node.key)
        preorder_traverse(node.left)
        preorder_traverse(node.right)

def postorder_traverse(node):
    if node is not None:
        postorder_traverse(node.left)
        postorder_traverse(node.right)
        print(node.key)

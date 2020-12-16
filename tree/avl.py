import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(bst.BST):
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            elif x is y.parent.right:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)
        
    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            elif x is y.parent.right:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= height(node.right) + 2:
                if height(node.left.left) < height(node.left.right):
                    self.left_rotate(node.left)
                self.right_rotate(node)
            elif height(node.right) >= height(node.left) + 2:
                if height(node.right.right) < height(node.right.left):
                    self.right_rotate(node.right)
                self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        node = super(AVL, self).insert(k)
        print(node)
        self.rebalance(node)

    def delete(self, k):
        node = super(AVL, self).delete(k)
        self.rebalance(node.parent)
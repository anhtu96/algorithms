from bst import *
from avl import *

# create tree
tree = BST()
to_insert_list = [15, 18, 6, 17, 20, 3, 7, 2, 4, 13, 9]
for k in to_insert_list:
    tree.insert(k)

# test traversal
def test_traversal(tree, method_name):
    if method_name == 'inorder':
        method = inorder_traverse
    elif method_name == 'preorder':
        method = preorder_traverse
    elif method_name == 'postorder':
        method = postorder
    method(tree.root)

# test_traversal(tree, 'inorder')

# test AVL
avl = AVL()
for k in to_insert_list:
    avl.insert(k)

# test_traversal(avl, 'inorder')
# test_traversal(tree, 'inorder')
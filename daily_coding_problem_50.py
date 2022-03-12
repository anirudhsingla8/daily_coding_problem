"""
This problem was asked by Microsoft.
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal Node is one of +,*,-,/.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
  +    +
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def calculateExpression(node):
    if not node:
        return None
    if node.left is None and node.right is None:
        return int(node.val)

    left_val = calculateExpression(node.left)
    right_val = calculateExpression(node.right)

    if node.val == "+":
        return left_val+right_val
    elif node.val == "*":
        return left_val*right_val
    elif node.val == "-":
        return left_val-right_val
    else:
        return left_val/right_val

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('20')
print(calculateExpression(root))
"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class unival:
    def __init__(self):
        self.count = 0

    def getCount(self, root):
        if not root:
            return False
        self.helper(root)
        return self.count

    def helper(self, node):
        if not node:
            return True
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left == False or right == False:
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        self.count += 1
        return True


root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.right = Node(0)
root.right.right.left = Node(0)
root.right.right.right = Node(0)
root.right.left = Node(1)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

initiator = unival()
ans = initiator.getCount(root)
print(ans)
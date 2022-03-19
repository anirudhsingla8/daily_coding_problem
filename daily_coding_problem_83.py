"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

# solved on https://leetcode.com/problems/invert-binary-tree/submissions/

class newNode:
    def __init__(self, val):
        left = None
        right = None
        data = val

class Tree:
    def invertTree(self, root):
        if not root:
            return None
        self.helper(root)
        return root

    def helper(self, node):
        if not node:
            return None
        left = self.helper(node.left)
        right = self.helper(node.right)
        node.left, node.right = right, left
        return node


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
invert = Tree()
ans = invert.invertTree(root)
print(ans)

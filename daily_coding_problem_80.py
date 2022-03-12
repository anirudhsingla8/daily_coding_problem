"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

"""


class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.maxLevel = 0
        self.ans = None

    def deepestNode(self, root):
        self.helper(root, 0)
        return self.ans

    def helper(self, node, level):
        if node is None:
            return None
        if level > self.maxLevel:
            self.maxLevel = level
            self.ans = node.val
        self.helper(node.left, level + 1)
        self.helper(node.right, level + 1)

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.right.left = newNode(5)
root.right.right = newNode(6)
root.right.left.right = newNode(7)
root.right.right.right = newNode(8)
root.right.left.right.left = newNode(9)
deep = Tree()
ans = deep.deepestNode(root)
print(ans)

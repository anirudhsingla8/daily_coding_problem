"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.ans = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            curr = self.root
            while curr:
                if curr.val < val:
                    if curr.right == None:
                        curr.right = Node(val)
                        return self
                    curr = curr.right
                else:
                    if curr.left == None:
                        curr.left = Node(val)
                        return self
                    curr = curr.left

    def findKthLargest(self, k):
        curr = self.root
        idx = [k]
        return self.helper(curr, idx)

    def helper(self, node, idx):
        if not node:
            return None
        right_node = self.helper(node.right, idx)
        if right_node:
            return right_node
        idx[0] -= 1
        if idx[0] == 0:
            return node.val
        left_node = self.helper(node.left, idx)
        if left_node:
            return left_node
        return None


bst = BinaryTree()
bst.insert(6)
bst.insert(2)
bst.insert(7)
bst.insert(7)
k = 4
print(bst.findKthLargest(k))

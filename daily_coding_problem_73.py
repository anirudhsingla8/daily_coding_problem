"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def reverseList(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
ans = reverseList(head)
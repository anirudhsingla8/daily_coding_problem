"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        self.length = 0

    def add(self, data):
        if self.length == 0:
            self.head = Node(data)
            self.prev = self.head
        else:
            self.prev.next = Node(data)
            self.prev = self.prev.next
        self.length += 1


def reverse_list(list):
    prev = None
    curr = list.head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def find_intersection(ll1, ll2):

    # method1 reverse linked list and then traverse and find the intersection
    # curr1 = reverse_list(ll1)
    # curr2 = reverse_list(ll2)
    # while curr1 and curr2:
    #     if curr1.data == curr2.data:
    #         return curr1.data
    #     curr1 = curr1.next
    #     curr2 = curr2.next
    # return -1

    #method2
    curr1 = ll1.head
    curr2 = ll2.head
    if ll1.length == 0 or ll2.length == 0:
        return -1
    elif ll1.length > ll2.length:
        d = ll1.length - ll2.length
        for i in range(0, d):
            curr1 = curr1.next
    elif ll1.length < ll2.length:
        d = ll2.length - ll1.length
        for i in range(0, d):
            curr2 = curr2.next
    while curr1 and curr2:
        if curr1.data == curr2.data:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next
    return -1


ll1 = LinkedList()
ll1.add(3)
ll1.add(7)
ll1.add(8)
ll1.add(10)

ll2 = LinkedList()
ll2.add(99)
ll2.add(1)
ll2.add(8)
ll2.add(10)

ans = find_intersection(ll1, ll2)
print(ans)

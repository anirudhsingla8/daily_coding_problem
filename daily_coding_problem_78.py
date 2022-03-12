"""
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""

import heapq


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge(lists):
    curr = Node()
    head = curr
    heap = []
    for list in lists:
        print(list.val)
        if list:
            heapq.heappush(heap, (list.val, list))

    while heap:
        val, node = heapq.heappop(heap)
        print(val, node)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    return head.next


list1 = Node(1)
list1.next = Node(20)
list1.next.next = Node(22)

list2 = Node(13)
list2.next = Node(22)
list2.next.next = Node(34)

list3 = Node(8)
list3.next = Node(9)
list3.next.next = Node(10)

lists = [list1, list2, list3]
ans = merge(lists)
print ans.val

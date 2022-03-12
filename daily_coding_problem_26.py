"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list.
 k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
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

    def deleteKth(self, k):
        fast = self.head
        for i in range(0, k):
            fast = fast.next
        slow = self.head
        prev = None
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        if prev == None and slow.next == None:
            return prev
        elif prev == None and slow.next != None:
            prev = slow.next
            return prev
        else:
            prev.next = slow.next
        return self.head


ll1 = LinkedList()
ll1.add(3)
ll1.add(7)
ll1.add(8)
ll1.add(10)
ll1.add(31)
ll1.add(72)
ll1.add(81)
ll1.add(11)
k = 2

ans = ll1.deleteKth(k)
print(ans)

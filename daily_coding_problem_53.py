"""
This problem was asked by Apple.

Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1 = self.s2[::-1]
        self.s1.append(val)
        self.s2 = self.s1[::-1]
        self.s1 = []

    def dequeue(self):
        self.s2.pop()

q = queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.enqueue(3)
q.dequeue()
q.enqueue(4)
print(q.s2[::-1])
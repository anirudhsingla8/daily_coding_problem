"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class OrderLog:
    def __init__(self, n):
        self.circular = [None for x in range(n)]
        self.n = n
        self.pos = 0

    def record(self, order_id):
        self.circular[self.pos] = order_id
        self.pos += 1
        if self.pos == self.n:
            self.pos = 0

    def getIthElement(self, i):
        return self.circular[self.pos - i]


log = OrderLog(10)
for id in range(20):
    log.record(id)

print(log.getIthElement(10))

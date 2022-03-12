"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None

class Cache:
    def __init__(self, size):
        self.hash_map = {}
        self.base = Node(-1)
        self.head = self.base
        self.tail = self.base
        self.cache_size = size
        self.hash_size = 0

    def set(self, key, value):
        if key not in self.hash_map:
            new_node = Node(value)
            if self.hash_size < self.cache_size:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head.next
                self.head.next = temp.next
                temp.next.prev = self.head
                self.tail.next = new_node
                self.tail = new_node
        else:
            curr_node = self.hash_map[key]
            curr_prev = curr_node.prev
            curr_next = curr_node.next
            curr_prev.next = curr_next

    def get(self, key):

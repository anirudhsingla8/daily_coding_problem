"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from heapq import *
def minRooms(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    rooms = 0
    minheap = []
    for interval in intervals:
        while len(minheap) and interval[0] >= minheap[0]:
            heappop(minheap)
        heappush(minheap,interval[1])
        rooms = max(rooms,len(minheap))
    return rooms


intervals = [[4,5], [2,3], [2,4], [3,5]]
#intervals = [[70, 90], [80, 100], [90, 95], [95, 100]]
ans = minRooms(intervals)
print(ans)

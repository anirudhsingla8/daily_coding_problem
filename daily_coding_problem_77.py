"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

def mergeIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    ans = []
    n = len(intervals)
    for i in range(1,n):
        if intervals[i][1] <= end:
            end = max(end,intervals[i][1])
        else:
            ans.append((start,end))
            start = intervals[i][0]
            end = intervals[i][1]
    ans.append((start,end))
    return ans

intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
ans = mergeIntervals(intervals)
print ans

"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

"""

import heapq


def running_median(elements):
    ans = []
    max_h = []
    min_h = []
    for item in elements:
        if len(max_h) == 0:
            heapq.heappush(max_h, -item)
        elif len(max_h) == len(min_h):
            if item < min_h[0]:
                heapq.heappush(max_h, -item)
            else:
                temp = heapq.heappop(min_h)
                heapq.heappush(min_h, item)
                heapq.heappush(max_h, -temp)
        else:
            if len(max_h) > len(min_h):
                if item < -max_h[0]:
                    temp = abs(heapq.heappop(max_h))
                    heapq.heappush(min_h, temp)
                    heapq.heappush(max_h, -item)
                else:
                    heapq.heappush(min_h, item)

        if len(max_h) > len(min_h):
            ans.append(-max_h[0])
        else:
            ans.append(float((abs(max_h[0]) + min_h[0])) / 2)
    return ans


elements = [2, 1, 5, 7, 2, 0, 5]
ans = running_median(elements)
print ans
"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height.
 Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

def trap_water(elements):
    l_max = 0
    r_max = 0
    ans = 0
    left = 0
    right = len(elements)-1
    while left <= right:
        if elements[left] < elements[right]:
            if elements[left] > l_max:
                l_max = elements[left]
            else:
                ans += (l_max-elements[left])
            left+=1
        else:
            if elements[right] > r_max:
                r_max = elements[right]
            else:
                ans += (r_max - elements[right])
            right-=1
    return ans

elements=[3, 0, 1, 3, 0, 5]
ans = trap_water(elements)
print(ans)
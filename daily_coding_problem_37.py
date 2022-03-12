"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

import copy


def subsets(nums):
    subsets = []
    idx = 0
    current = []
    n = len(nums)
    helper(idx, nums, n, current, subsets)
    return subsets


def helper(idx, nums, n, current, subsets):
    new_arr = copy.deepcopy(current)
    subsets.append(new_arr)
    for i in range(idx, n):
        current.append(nums[i])
        helper(i + 1, nums, n, current, subsets)
        current.pop(-1)


nums = [1,2,3]
ans = subsets(nums)
print ans
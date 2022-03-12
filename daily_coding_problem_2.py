"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product(arr):
    n = len(arr)
    left_arr = []
    left = 1
    for x in arr:
        left_arr.append(x * left)
        left = left_arr[-1]
    right = 1
    for i in range(n - 1, -1, -1):
        if i - 1 >= 0:
            left_arr[i] = left_arr[i - 1] * right
            right = right * arr[i]
        else:
            left_arr[i] = right
    print(left_arr)


arr = [1, 2, 3, 4, 5]
ans = product(arr)

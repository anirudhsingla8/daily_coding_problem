"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def segregate(arr):
    left = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] < 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
    return left, arr[left:]


def firstMissing(arr):
    start, arr = segregate(arr)
    n = len(arr)
    for i in range(0, n):
        if 0 < arr[i] <= n - 1:
            arr[abs(arr[i] - 1)] = -arr[abs(arr[i] - 1)]

    for i in range(0, n):
        if arr[i] > 0:
            return i + 1
    return n


arr = [1, 2, 0]
ans = firstMissing(arr)
print(ans)

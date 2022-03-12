"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""


def LIS(arr):
    n = len(arr)
    dp = [1] * n
    count = 1
    for i in range(0, n):
        j = 0
        while j < i:
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            count = max(count,dp[i])
            j+=1
    return count


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
ans = LIS(arr)
print ans

"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to max_stackore the results.
You can simply print them out as you compute them
"""


def maxWindow(elements, k):
    n = len(elements)
    max_stack = []
    ans = []
    for i in range(0, k):
        while max_stack and elements[max_stack[-1]] < elements[i]:
            max_stack.pop()
        max_stack.append(i)

    for i in range(k, n):
        ans.append(elements[max_stack[0]])
        while max_stack and max_stack[0] <= i - k:
            max_stack.pop(0)
        while max_stack and elements[max_stack[-1]] < elements[i]:
            max_stack.pop()
        max_stack.append(i)
    ans.append(elements[max_stack[0]])
    return ans


elements = [10, 5, 2, 7, 8, 7]
k = 3
ans = maxWindow(elements, k)
print(ans)

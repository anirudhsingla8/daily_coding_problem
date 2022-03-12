"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def maximumSum(element):
    n = len(element)
    if n <= 2:
        return max(element)
    a = element[0]
    b = max(element[0],element[1])
    max_ans = max(a,b)
    for i in range(2,n):
        max_ans = max(b, element[i] + a)
        a = b
        b = max_ans
    return max_ans

element=[2, 4, 6, 2, 5]
#element = [5,1,1,5]
ans = maximumSum(element)
print(ans)

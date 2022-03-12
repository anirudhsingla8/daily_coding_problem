"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""


def subset(elements):
    n = len(elements)
    row = n
    total_elements_sum = sum(elements)
    if total_elements_sum % 2 != 0:
        return False
    col = (total_elements_sum // 2) + 1
    dp = [[0 for x in range(col)] for x in range(row)]
    for i in range(1, col):
        if elements[0] == i:
            dp[0][i] = 1
    for i in range(1, row):
        for j in range(1, col):
            if j==0:
                dp[i][j] = 0
            elif dp[i-1][j] == 1:
                dp[i][j] = 1
            else:
                if j-elements[i]>=0 and dp[i-1][j-elements[i]] == 1:
                    dp[i][j] = 1

    if dp[row-1][col-1] == 1:
        return True
    return False


elements = [2,13,1]
print(subset(elements))
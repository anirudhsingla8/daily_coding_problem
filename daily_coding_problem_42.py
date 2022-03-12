"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""


def getSubsets(elements, k):
    row = len(elements)
    dp = [[0 for x in range(k + 1)] for x in range(row)]
    for i in range(row):
        dp[i][0] = 1
    for i in range(row):
        for j in range(k + 1):
            if j == 0:
                continue
            if j == elements[i]:
                dp[i][j] = 1
            else:
                if i > 0:
                    if dp[i - 1][j] == 1:
                        dp[i][j] = 1
                    if j >= elements[i] and dp[i - 1][j - elements[i]] == 1:
                        dp[i][j] = 1

    print(dp)


elements = [3,4,1,8,2,5]
k = 10
ans = getSubsets(elements, k)
print(ans)

"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M,
write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

def paths(n):
    dp = [[1 for x in range(n)] for x in range(n)]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][n-1]

n = 600
ans = paths(n)
print(ans)
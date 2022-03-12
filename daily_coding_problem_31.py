"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions,
and substitutions required to change one string to the other.
For example,
the edit distance between "kitten" and "sitting" is three: substitute the "k for "s", substitute the "e" for "i", and append a "g".

Given two strings, compute the edit distance between them.
"""


def edit_distance(str1, str2):
    row = len(str1)
    col = len(str2)
    dp = [[0 for x in range(0, col + 1)] for x in range(0, row + 1)]
    for i in range(0, row + 1):
        for j in range(0, col + 1):
            if i == 0:
                dp[i][j] = j
                continue
            if j == 0:
                dp[i][j] = i
                continue
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    return dp[row][col]


str1 = "abc"
str2 = "bcd"
ans = edit_distance(str1, str2)
print(ans)

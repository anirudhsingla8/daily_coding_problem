"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""


def palindrome(elements):
    n = len(elements)
    dp = [[0 for x in range(n)] for x in range(n)]
    x,y = 0,0
    max_len = 1
    for i in range(0, n):
        dp[i][i] = 1

    for i in range(0, n - 1):
        if elements[i] == elements[i + 1]:
            dp[i][i + 1] = 1
            max_len = max(max_len,2)
            x,y = i,i+1

    for i in range(2, n):
        for j in range(i, n):
            if elements[j-i] == elements[j] and dp[j-i+1][j-1] == 1:
                dp[j-i][j] = 1
                max_len = i+1
                x,y = j-i,j
    print(max_len)
    return elements[x:y+1]


elements = "aabcdcb"
ans = palindrome(elements)
print(ans)

"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def distinct(s, k):
    start = 0
    ans = 0
    n = len(s)
    element_map = {}
    for end in range(0, n):
        if s[end] not in element_map:
            element_map[s[end]] = 0
        element_map[s[end]] += 1
        while len(element_map) > k:
            element_map[s[start]] -= 1
            if element_map[s[start]] == 0:
                del element_map[s[start]]
            start += 1
        ans = max(ans, end - start)
    return ans

s = "abcba"
k = 2
ans = distinct(s, k)
print (ans)

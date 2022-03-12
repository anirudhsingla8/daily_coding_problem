"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

def unique(elements):
    ans = 0
    n = len(elements)
    for i in range(32):
        p = 0
        for j in range(0,n):
            if (elements[j] & (1 << i)) != 0:
                p+=1
        p %= k
        ans += pow(2,i) * p
    return ans

elements = [2,2,1,1,11,4,4,6,5,6,5]
k = 2
ans = unique(elements)
print(ans)
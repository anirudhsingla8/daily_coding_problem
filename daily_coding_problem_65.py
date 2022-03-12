"""
This problem was asked by Amazon.
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""


def spiral(elements):
    left = 0
    right = len(elements[0])
    top = 0
    bottom = len(elements)
    ans = []
    while left < right and top < bottom:
        for i in range(left, right):
            ans.append(elements[top][i])
        top += 1

        for i in range(top, bottom):
            ans.append(elements[i][right-1])
        right -= 1

        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                ans.append(elements[bottom - 1][i])
            bottom -= 1

        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                ans.append(elements[i][left])
            left += 1
    return ans


elements = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]
ans = spiral(elements)
print(ans)

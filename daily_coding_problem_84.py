"""
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water,
so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def traverse(elements, i, j, row, col):
    if i < 0 or i >= row or j < 0 or j >= col or elements[i][j] != 1:
        return
    elements[i][j] = 2
    traverse(elements, i - 1, j, row, col)
    traverse(elements, i + 1, j, row, col)
    traverse(elements, i - 1, j - 1, row, col)
    traverse(elements, i + 1, j - 1, row, col)
    traverse(elements, i, j - 1, row, col)
    traverse(elements, i - 1, j + 1, row, col)
    traverse(elements, i + 1, j + 1, row, col)
    traverse(elements, i, j + 1, row, col)


def islands(elements):
    count = 0
    row = len(elements)
    col = len(elements[0])
    for i in range(0, row):
        for j in range(0, col):
            if elements[i][j] != 1:
                continue
            else:
                count += 1
                traverse(elements, i, j, row, col)
    return count


elements = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
ans = islands(elements)
print(ans)

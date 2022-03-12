"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
 return the minimum number of steps required to reach the end coordinate from the start.
 If there is no possible path, then return null. You can move up, left, down, and right.
 You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""


class Traverse:
    def __init__(self, path, finalGoal):
        self.path = path
        self.find = False
        self.steps = -1
        self.finalGoal = finalGoal

    def getSteps(self, start, end):
        row = len(self.path)
        col = len(self.path[0])
        self.helper(start, end, row, col, 0)
        return self.steps

    def helper(self, start, end, row, col, val):
        if start < 0 or start >= row or end < 0 or end >= col or self.find == True \
                or self.path[start][end] == "t" or self.path[start][end] != "f":
            return
        self.path[start][end] = val
        if [start, end] == self.finalGoal:
            self.find = True
            self.steps = val
            return
        self.helper(start - 1, end, row, col, val + 1)
        self.helper(start, end + 1, row, col, val + 1)
        self.helper(start + 1, end, row, col, val + 1)
        self.helper(start, end - 1, row, col, val + 1)


# path = [["f", "f", "f", "f"],
#         ["t", "t", "f", "t"],
#         ["f", "f", "f", "f"],
#         ["f", "f", "f", "f"]]

path = [
    ["f", "f", "f", "t"],
    ["t", "f", "t", "f"],
    ["t", "f", "f", "t"],
    ["t", "f", "t", "f"],
    ["t", "f", "f", "t"],
    ["t", "f", "t", "f"]
]
start = 1
end = 0
finalGoal = [0, 0]

traverse = Traverse(path, finalGoal)
ans = traverse.getSteps(start, end)
print(ans)

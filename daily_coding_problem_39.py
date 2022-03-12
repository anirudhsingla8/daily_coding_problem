"""
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (1) and a dead cell with a dot (0).
"""


def gameOfLife(board):
    row = len(board)
    col = len(board[0])
    for i in range(0, row):
        for j in range(0, col):
            helper(i, j, row, col, board)
    for i in range(0, row):
        for j in range(0, col):
            if board[i][j] == "N":
                board[i][j] = 1
            elif board[i][j] == "P":
                board[i][j] = 0


def helper(i, j, row, col, board):
    count = 0
    r_val = [1, -1, 0, 1, -1, 0, 1, -1]
    c_val = [0, 0, -1, -1, -1, 1, 1, 1]
    n = 8
    for x in range(n):
        if validate(i + r_val[x], j + c_val[x], row, col):
            if board[i + r_val[x]][j + c_val[x]] == 1 or board[i + r_val[x]][j + c_val[x]] == "P":
                count += 1
    if board[i][j] == 0:
        if count == 3:
            board[i][j] = "N"
    else:
        if count < 2:
            board[i][j] = "P"
        elif count > 3:
            board[i][j] = "P"


def validate(i, j, row, col):
    if 0 <= i < row and j >= 0 and j < col:
        return True
    return False


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(board)
print(board)

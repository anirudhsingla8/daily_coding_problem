"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""

"""
def minCost(costs):
    row = len(costs)
    col = len(costs[0])
    for i in range(1, row):
        for j in range(0, col):
            minn = float('inf')
            for k in range(0, col):
                if j != k:
                    minn = min(minn, costs[i - 1][k])
            costs[i][j] += minn
    return min(costs[row - 1])
    
    timeComplexity: O(row*col*col)
"""


def minCost(costs):
    row = len(costs)
    col = len(costs[0])
    firstLeast = float("inf")
    secondLeast = float("inf")
    for j in range(0, col):
        if costs[0][j] <= firstLeast:
            secondLeast = firstLeast
            firstLeast = costs[0][j]
        elif costs[0][j] <= secondLeast:
            secondLeast = costs[0][j]

    for i in range(1, row):
        newFirstLeast = float("inf")
        newSecondLeast = float("inf")
        for j in range(0, col):
            if costs[i-1][j] == firstLeast:
                costs[i][j] += secondLeast
            else:
                costs[i][j] += firstLeast

            if costs[i][j] <= newFirstLeast:
                newSecondLeast = newFirstLeast
                newFirstLeast = costs[i][j]
            elif costs[i][j] <= newSecondLeast:
                newSecondLeast = costs[i][j]
        firstLeast = newFirstLeast
        secondLeast = newSecondLeast
    return min(costs[row - 1])
    # timeComplexity: O(row*col)

costs = [[1, 5, 7, 2, 3, 4],
         [5, 8, 4, 3, 6, 1],
         [3, 2, 9, 7, 2, 3],
         [1, 2, 4, 9, 1, 7]]
ans = minCost(costs)
print(ans)

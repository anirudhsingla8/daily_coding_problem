"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def maxProduct(elements):
    maxA = -float("inf")
    maxB = -float("inf")
    maxC = -float("inf")
    minA = float("inf")
    minB = float("inf")
    for x in elements:
        if x > maxA:
            maxC = maxB
            maxB = maxA
            maxA = x
        elif x > maxB:
            maxC = maxB
            maxB = x
        elif x > maxC:
            maxC = x

        if x < minA:
            minB = minA
            minA = x
        elif x < minB:
            minB = x

    return max(minA * minB * maxA, maxA * maxB * maxC)


elements = [-10, -10, 5, 2]
ans = maxProduct(elements)
print ans

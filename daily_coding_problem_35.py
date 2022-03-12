"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
 the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def arrange(elements):
    left = 0
    mid = 0
    right = len(elements) - 1
    while mid <= right:
        if elements[mid] == "R":
            elements[mid], elements[left] = elements[left], elements[mid]
            left += 1
            mid += 1
        elif elements[mid] == "B":
            elements[mid], elements[right] = elements[right], elements[mid]
            right -= 1
        else:
            mid += 1


elements = ["R","B",'G', 'B', 'R', 'R', 'B', 'R', 'G']
arrange(elements)
print elements

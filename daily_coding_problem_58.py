"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def findElement(elements, target):
    left = 0
    right = len(elements) - 1
    # if elements[left] == element:
    #     return left
    # if elements[right] == element:
    #     return right
    while left <= right:
        mid = (left + right) // 2
        if elements[mid] == target:
            return mid
        if elements[mid] >= elements[left]:
            if target >= elements[left] and target <= elements[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= elements[mid] and target <= elements[right]:
                left = mid + 1
            else:
                right = mid - 1
    return None


elements = [13, 18, 25, 2, 8, 10, 11, 12]
target = 2
ans = findElement(elements, target)
print(ans)

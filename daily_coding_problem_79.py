"""
This problem was asked by Facebook.

Given an array of integers,
write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true,
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""


def checkPossibility(nums):
    n = len(nums)
    if n <= 2:
        return True
    count = (1 if nums[0] > nums[1] else 0)
    for i in range(1, n - 1):
        if nums[i] > nums[i + 1]:
            if nums[i - 1] > nums[i + 1]:
                nums[i + 1] = nums[i]
            if count == 1:
                return False
            count += 1
    return True

elements = [10,5,7]
ans = checkPossibility(elements)
print ans

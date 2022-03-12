"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""


def mergeSortedArray(count, left_arr, right_arr):
    i = 0
    j = 0
    k = 0
    len_left = len(left_arr)
    len_right = len(right_arr)
    merged_arr = [0] * (len_left + len_right)

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            merged_arr[k] = left_arr[i]
            k += 1
            i += 1
        else:
            count[0] += len_left - i
            merged_arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len_left:
        merged_arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        merged_arr[k] = right_arr[j]
        j += 1
        k += 1

    return merged_arr

def mergeSort(elements, count, left, right):
    if left == right:
        return [elements[left]]

    mid = (left + right) // 2
    left_arr = mergeSort(elements, count, left, mid)
    right_arr = mergeSort(elements, count, mid + 1, right)
    merged = mergeSortedArray(count, left_arr, right_arr)
    return merged


elements = [1, 1, 1, 2, 2]
n = len(elements)
count = [0]
mergeSort(elements, count, 0, n-1)
print(count)

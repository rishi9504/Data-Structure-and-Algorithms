import random
def quickSort(arr):
    """
    Sorts an array using the quicksort algorithm.

    The quicksort algorithm works by selecting a 'pivot' element from the array and
    partitioning the other elements into two sub-arrays, according to whether they
    are less than or greater than the pivot. The sub-arrays are then recursively
    sorted.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    :param arr: The array to be sorted
    :return: The sorted array
    """
    
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)

print (quickSort([3,6,8,10,1,2,1]))
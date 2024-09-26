def orderedLinearSearch(arr, target):
    
    """
    Searches a sorted array for a given target element.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param arr: The sorted array to search
    :param target: The target element to search for
    :return: The index of the element if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return -1
    return -1
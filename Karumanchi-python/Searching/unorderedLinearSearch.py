def unorderedLinearSearch(arr, x):
    """
    Searches an array for an element x.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param arr: The array to search
    :param x: The element to search for
    :return: True if x is in arr, False otherwise
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return True 

    return False

print(unorderedLinearSearch([3,6,8,10,1,2,1],7))
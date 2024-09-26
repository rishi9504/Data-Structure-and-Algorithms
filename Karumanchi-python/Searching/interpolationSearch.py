def interpolationSearch(arr,val):

    """
    Searches a sorted array using interpolation search.

    Interpolation search is an improvement over binary search for instances, where
    the values in the array are uniformly distributed. Binary search always goes
    to the middle element to compare, but interpolation search may go to different
    locations according to the value of key being searched.

    Time Complexity: O(log log n)
    Space Complexity: O(1)

    :param arr: A sorted array
    :param val: The element to search for
    :return: The index of the element if found, None otherwise
    """
    low = 0
    high = len(arr)-1

    while arr[low] <= val <= arr[high]:
        mid = low + (val - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[mid]<val:
            low = mid+1
        elif arr[mid]>val:
            high = mid-1
        else:
            return mid
    if arr[low] == val:
        return low
    return None        

print (interpolationSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
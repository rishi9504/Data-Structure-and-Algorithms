def selectionSort(arr):
    """
    Sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
    The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selectionSort([64, 34, 25, 12, 22, 11, 90]))
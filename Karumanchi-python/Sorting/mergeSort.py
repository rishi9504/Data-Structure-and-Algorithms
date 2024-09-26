def mergeSort(arr):

    
    """
    Sorts an array by dividing it into two halves, sorting them individually using recursion, and then merging them.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    :param arr: The array to be sorted
    :return: The sorted array
    """
    
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the first and second halves
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

print (mergeSort([64, 34, 25, 12, 22, 11, 90]))
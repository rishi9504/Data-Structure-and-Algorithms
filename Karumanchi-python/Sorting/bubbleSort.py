def bubbleSort(arr):

    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print (bubbleSort([64, 34, 25, 12, 22, 11, 90]))

def betterBubbleSort(arr):

    """
    Sorts an array by repeatedly swapping the adjacent elements if they are in wrong order.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    :param arr: The array to be sorted
    :return: The sorted array
    """
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

    return arr

print (betterBubbleSort([64, 34, 25, 12, 22, 11, 90]))
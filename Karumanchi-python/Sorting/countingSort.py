import random

# Counting Sort
def countingSort(arr,k):
    """
    Sorts an array using the counting sort algorithm.

    The counting sort algorithm works by creating an array of counts, where each index
    in the array corresponds to a value in the input array. The counts are then used
    to determine the proper position of each element in the sorted array.

    Time Complexity: O(n + k)
    Space Complexity: O(n + k)

    :param arr: The array to be sorted
    :param k: The maximum value in the array
    :return: The sorted array
    """

    b= [0 for el in arr]
    c = [0 for el in range(0,k+1)]

    for i in range(0,len(arr)):
        c[arr[i]] += 1

    for i in range(1,len(c)):
        c[i] += c[i-1]

    for i in range(len(arr)-1,-1,-1):
        b[c[arr[i]]-1] = arr[i]
        c[arr[i]] -= 1

    for i in range(0,len(arr)):
        arr[i] = b[i]

    return arr

print (countingSort([3,6,8,10,1,2,1],10))
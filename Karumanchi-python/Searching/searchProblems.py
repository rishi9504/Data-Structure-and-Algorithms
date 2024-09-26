# check duplicates in array using negation technique

import math
def checkDuplicates(arr):
    arr.sort()

    for i in range(0,len(arr)):
        if arr[abs(arr[i])] < 0 :
            return True
        else:
            arr[abs(arr[i])] = -arr[abs(arr[i])]

    return False

print (checkDuplicates([3,6,8,10,1,2,1]))


# given an array on n numbers, find the element which appears the max numbers of the time

def maxElement(arr):
    """
    Finds the element which appears the maximum number of times in a given array.

    Parameters:
        arr (list): The array to search for the maximum element

    Returns:
        int: The maximum element
    """

    table ={}
    max=0

    for i in arr:

        if i in table:
            table[i]+=1

        else:
            table[i]=1

    for i in table:

        if table[i]>max:
            max=table[i]

    return max



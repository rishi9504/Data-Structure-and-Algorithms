# check for duplicates in array using sorting

def checkDuplicates(arr):

    arr.sort()

    for i in range(len(arr)-1):

        if arr[i] == arr[i+1]:
            return True

    return False

print(checkDuplicates([3,6,8,10,1,2,1]))

# given a sorted array of numbers, find if a given number is present in the array

def binarySearch(arr, l, r, x):

    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return True

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return False
    

# Given an array a[0...n-1] where each element of the array represents a vote in the election.
# Find the candidate who got maximum votes.
# 
# Time Complexity: O(nlogn)
# Can be further optimized using counting sort

def findCandidate(arr, n):
    """
    Finds the candidate with the maximum votes in an election.

    Parameters:
        arr (list): A sorted list of votes where each element of the list represents a vote in the election.
        n (int): The number of votes in the array.

    Time Complexity: O(nlogn)

    Returns:
        int: The candidate with the maximum votes.
    """
    arr.sort()
    count = maxCounter = 0
    candidate = maxCandidate = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
        else:
            count = 1
            candidate = arr[i]
        if count > maxCounter:
            maxCandidate = arr[i]
            maxCounter = count
    return maxCandidate

print(findCandidate([3,6,8,10,1,2,1],7))


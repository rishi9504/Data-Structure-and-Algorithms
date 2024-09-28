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


# given a list of numbers, find the missing number

def missingNumber(arr):

    """
    Finds the missing number in a given list of numbers.

    The missing number is the one which is not present in the array.

    Parameters:
        arr (list): The array to search for the missing number

    Returns:
        int: The missing number


            """

    n = len(arr)
    X=0

    for i in range(0,n+2):

        X = X^i

    for i in range(0,n):

        X = X^arr[i]

    return X

print (missingNumber([8,2,1,4,6,5,7,9]))

# find the two repeating elements in a given array

def twoRepeatingElements(arr):
    seen = set()
    for num in arr:
        if num in seen:
            print(num)
        else:
            seen.add(num)

print(twoRepeatingElements([3,5,7,4,2,4,2,1,9]))

# given an array of n numbers, find two elements in the array whose sum is equal to the given number k.

def twoSum(arr,k):
    """
    Finds two elements in the array whose sum is equal to the given number k.

    Parameters:
        arr (list): The array to search for the two elements
        k (int): The target sum

    Returns:
        list: The two elements in the array whose sum is equal to the given number k

    """
    table = {}
    for i in range(0,len(arr)):
        if arr[i] in table:
            return [table[arr[i]],i]
        else:
            table[k-arr[i]]=i

print(twoSum([10,20,10,40,50,60,70],50))



# This function finds two elements in an array that add up to a given target sum `k`. It uses a hash table to store the elements it has seen so far and their indices. For each element, it checks if its complement (i.e., the value that would add up to `k`) is already in the table. If it is, it returns the two elements. If not, it adds the current element to the table.

# given an array of n elements. Find three indices such that a[i]^2 + a[j]^2 = a[k]^2


def threeSumSquare(arr,k):

    """
    Finds three indices such that a[i]^2 + a[j]^2 = a[k]^2

    Parameters:
        arr (list): The array to search for the three indices
        k (int): The target sum

    Returns:
        list: The three indices such that a[i]^2 + a[j]^2 = a[k]^2

    """

    table = {}

    for i in range(0,len(arr)):

        for j in range(i+1,len(arr)):

            if (arr[i]**2 + arr[j]**2) == k:
                return [i,j]

            elif (arr[i]**2 + arr[j]**2) < k:

                table[arr[i]**2 + arr[j]**2] = [i,j]

    for i in range(0,len(arr)):

        for j in range(i+1,len(arr)):   

            if (arr[i]**2 + arr[j]**2) in table:

                return [table[arr[i]**2 + arr[j]**2][0],table[arr[i]**2 + arr[j]**2][1],i,j]

print(threeSumSquare([10,20,10,40,50,60,70],50))

# given an array of n elements. Find two elements whose sum is closest to zero

def twoElementsClosestToZero(arr):
    if arr is None or len(arr) < 2:
        return None
    arr.sort()
    l = 0
    r = len(arr) - 1
    ml = 0
    mr = len(arr) - 1
    ms = float('inf')
    while l < r:
        s = arr[l] + arr[r]
        if abs(s) < abs(ms):
            ms = s
            ml = l
            mr = r
        if s < 0:
            l += 1
        else:
            r -= 1
    return [arr[ml], arr[mr]] 

print (twoElementsClosestToZero([1,60,-10,70,-80,85]))               


# given an array of n elements. Find the majority element. A majority element is an element that appears more than n/2 times.


def majorityElement(arr):
    """
    Finds the majority element in an array.

    A majority element is an element that appears more than n/2 times.

    Parameters:
        arr (list): The array to search for the majority element

    Returns:
        int: The majority element
    """
    if arr is None or len(arr) < 2:
        return None
    count = 1
    majority = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == majority:
            count += 1
        else:
            count -= 1
            if count == 0:
                majority = arr[i]
                count = 1
    return majority

print (majorityElement([1, 2, 5, 2, 5, 2, 5, 3, 5]))
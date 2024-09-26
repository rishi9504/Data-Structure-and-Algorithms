def insertionSort(arr):
    """
    Sorts an array by repeatedly inserting each element into the sorted subarray.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucketSort(arr):
    """
    Sorts an array using the bucket sort algorithm.

    The bucket sort algorithm works by creating a list of buckets, where each
    bucket is an array. The algorithm then iterates through the array and places
    each element in the appropriate bucket.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    :param arr: The array to be sorted
    :return: The sorted array
    """
    if len(arr) <= 1:
        return arr

    # Create a list of buckets
    buckets = [[] for _ in range(len(arr))]

    # Place each element in the appropriate bucket
    for i in arr:
        j = int(i * len(arr))
        buckets[j].append(i)

    # Sort each bucket
    for i in range(len(buckets)):
        buckets[i] = insertionSort(buckets[i])

    # Concatenate the buckets
    result = []
    for i in range(len(buckets)):
        result.extend(buckets[i])

    return result

print (bucketSort([0.42, 0.32, 0.99, 0.08, 0.2, 0.16, 0.52, 0.92, 0.72, 0.62]))
def iterativeBinarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print (iterativeBinarySearch([2, 3, 4, 10, 40], 0, 4, 10))

def recursiveBinarySearch(arr, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return recursiveBinarySearch(arr, mid + 1, r, x)
        else:
            return recursiveBinarySearch(arr, l, mid - 1, x)
        
print (recursiveBinarySearch([2, 3, 4, 10, 40], 0, 4, 10))        
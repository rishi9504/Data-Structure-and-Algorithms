# PATTERN 1: TWO POINTERS FROM OPPOSITE ENDS
# Common uses: 
# - Two Sum problem (sorted array)
# - Container With Most Water
# - Trapping Rain Water
# - Valid Palindrome

def two_pointers_opposite_ends(arr):
    left, right = 0, len(arr) - 1
    result = []
    
    while left < right:
        # Process current elements
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            # Found what we're looking for
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
            
            # Optional: Skip duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < target:
            # Need a larger sum, move left pointer right
            left += 1
        else:
            # Need a smaller sum, move right pointer left
            right -= 1
    
    return result


# PATTERN 2: FAST AND SLOW POINTERS
# Common uses:
# - Linked List Cycle Detection
# - Finding cycle start point
# - Middle of Linked List
# - Palindrome Linked List

def fast_slow_pointers(head):
    if not head or not head.next:
        return False
    
    # Initialize pointers
    slow = head
    fast = head
    
    # Move pointers until they meet or fast reaches end
    while fast and fast.next:
        slow = slow.next          # Move slow one step
        fast = fast.next.next     # Move fast two steps
        
        # Cycle detected
        if slow == fast:
            return True
    
    # No cycle if fast reached end
    return False


# PATTERN 3: SLIDING WINDOW / SAME DIRECTION POINTERS
# Common uses:
# - Maximum/Minimum Subarray of size K
# - Longest Substring Without Repeating Characters
# - Minimum Window Substring

def sliding_window(arr, k):
    n = len(arr)
    left = 0
    current_sum = 0
    max_sum = float('-inf')
    
    for right in range(n):
        # Expand window by including right element
        current_sum += arr[right]
        
        # When window size becomes k
        if (right - left + 1) == k:
            # Update result
            max_sum = max(max_sum, current_sum)
            
            # Shrink window from left
            current_sum -= arr[left]
            left += 1
    
    return max_sum


# PATTERN 4: MERGE TWO SORTED ARRAYS/LISTS
# Common uses:
# - Merge Sorted Arrays
# - Intersection of Arrays
# - Merge Sorted Lists

def merge_two_sorted_arrays(nums1, m, nums2, n):
    # Set pointers to the end of valid elements in nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # Set pointer to the end of the merged array
    p = m + n - 1
    
    # Merge from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, add them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
        
    return nums1


# PATTERN 5: THREE POINTERS (VARIATION)
# Common uses:
# - 3Sum problem
# - 3Sum Closest

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first pointer
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Use two-pointer technique for the remaining array
        left = i + 1
        right = n - 1
        target = -nums[i]  # Looking for pairs that sum to -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return result


# PATTERN 6: DUTCH NATIONAL FLAG (3-way partition)
# Common uses:
# - Sort Colors
# - Partition Array

def sort_colors(nums):
    # Initialize pointers
    low = 0        # Boundary for 0s
    mid = 0        # Current element
    high = len(nums) - 1  # Boundary for 2s
    
    # Process array
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low pointer, advance both
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is in the right place, just move mid
            mid += 1
        else:  # nums[mid] == 2
            # Swap with high pointer, only move high
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums

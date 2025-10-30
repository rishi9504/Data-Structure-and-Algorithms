# SLIDING WINDOW TEMPLATE 1: FIXED SIZE WINDOW
# Use when the window size is fixed (e.g., find max sum subarray of size k)

def fixed_size_sliding_window(arr, k):
    n = len(arr)
    
    # Edge case: if array is smaller than window size
    if n < k:
        return None
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window from left to right
    for i in range(k, n):
        # Add the incoming element and remove the outgoing element
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


# SLIDING WINDOW TEMPLATE 2: VARIABLE SIZE WINDOW - EXPANSION & CONTRACTION
# Use when looking for a subarray that satisfies a condition

def variable_size_sliding_window(arr, target):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        # Expand the window by including the right element
        current_sum += arr[right]
        
        # Contract the window from the left as long as the condition is satisfied
        while current_sum >= target:
            # Update result
            min_length = min(min_length, right - left + 1)
            
            # Shrink window from left
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


# SLIDING WINDOW TEMPLATE 3: USING HASHMAP FOR SUBSTRING PROBLEMS
# Used for problems involving distinct characters or frequency constraints

def sliding_window_with_hashmap(s, k):
    n = len(s)
    left = 0
    max_length = 0
    char_frequency = {}  # Hashmap to store character frequencies
    
    for right in range(n):
        # Process the current character
        char_right = s[right]
        char_frequency[char_right] = char_frequency.get(char_right, 0) + 1
        
        # Contract window until the window is valid
        # Example condition: while len(char_frequency) > k 
        # (more than k distinct characters)
        while len(char_frequency) > k:
            char_left = s[left]
            char_frequency[char_left] -= 1
            
            # Remove character from map if its count becomes 0
            if char_frequency[char_left] == 0:
                del char_frequency[char_left]
                
            left += 1
        
        # Update result - at this point, window has at most k distinct characters
        max_length = max(max_length, right - left + 1)
    
    return max_length


# SLIDING WINDOW TEMPLATE 4: USING COUNTER FOR ANAGRAM/PATTERN MATCHING
# Used for problems like "find all anagrams" or "minimum window substring"

from collections import Counter

def sliding_window_pattern_matching(s, pattern):
    n, p = len(s), len(pattern)
    if n < p:
        return []
    
    # Create frequency counter for pattern
    pattern_count = Counter(pattern)
    window_count = Counter()
    
    left = 0
    matches = 0  # number of characters correctly matched
    required = len(pattern_count)  # number of unique characters to match
    results = []
    
    for right in range(n):
        # Add right character to window
        char_right = s[right]
        window_count[char_right] += 1
        
        # Check if the frequency of this character matches with pattern
        if char_right in pattern_count and window_count[char_right] == pattern_count[char_right]:
            matches += 1
        
        # If the window size exceeds pattern length, shrink from left
        if right - left + 1 > p:
            char_left = s[left]
            
            # If this was a matched character and we're breaking the match
            if char_left in pattern_count and window_count[char_left] == pattern_count[char_left]:
                matches -= 1
                
            window_count[char_left] -= 1
            left += 1
        
        # Check if we found an anagram (all characters match in frequency)
        if right - left + 1 == p and matches == required:
            results.append(left)
    
    return results


# SLIDING WINDOW TEMPLATE 5: DYNAMIC CRITERIA WINDOW
# For problems where the criteria changes as the window expands/contracts
# Example: Longest Substring with At Most K Replacements

def sliding_window_dynamic_criteria(s, k):
    n = len(s)
    left = 0
    max_length = 0
    max_count = 0  # Count of the most frequent character in current window
    char_frequency = {}
    
    for right in range(n):
        # Process current character
        char_right = s[right]
        char_frequency[char_right] = char_frequency.get(char_right, 0) + 1
        
        # Update the count of most frequent character
        max_count = max(max_count, char_frequency[char_right])
        
        # Current window size - max frequency = number of characters we need to replace
        # If this is more than k, shrink window
        if (right - left + 1) - max_count > k:
            char_left = s[left]
            char_frequency[char_left] -= 1
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# EXAMPLE LEETCODE PROBLEMS FOR EACH TEMPLATE:

# Template 1: Fixed Size Window
# - LC 643: Maximum Average Subarray I
# - LC 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Template 2: Variable Size Window
# - LC 209: Minimum Size Subarray Sum
# - LC 862: Shortest Subarray with Sum at Least K (more complex version)

# Template 3: Using Hashmap
# - LC 3: Longest Substring Without Repeating Characters
# - LC 340: Longest Substring with At Most K Distinct Characters
# - LC 159: Longest Substring with At Most Two Distinct Characters  

# Template 4: Counter for Pattern Matching
# - LC 438: Find All Anagrams in a String
# - LC 76: Minimum Window Substring
# - LC 567: Permutation in String

# Template 5: Dynamic Criteria
# - LC 424: Longest Repeating Character Replacement
# - LC 1004: Max Consecutive Ones III

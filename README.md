# Data-Structure-and-Algorithms

### DP Patterns
#### Fibonacci Pattern
The Fibonacci number sequence is a classic example of dynamic programming (DP) because it involves overlapping subproblems that can be solved more efficiently by storing intermediate results to avoid redundant computations.

### Fibonacci Sequence:
The Fibonacci sequence is defined as:
- \( F(0) = 0 \)
- \( F(1) = 1 \)
- \( F(n) = F(n-1) + F(n-2) \) for \( n \geq 2 \)

### Problem:
We want to compute the \( n \)-th Fibonacci number.

### DP Pattern Explanation:
Dynamic programming is particularly useful for Fibonacci because it allows us to compute the result in a bottom-up manner, avoiding the exponential time complexity of a naive recursive solution.

### Two Main Approaches:

1. **Top-down with Memoization (Recursive DP)**:
   - Recursively compute the Fibonacci numbers, but use a cache (or memoization table) to store the results of previously computed Fibonacci numbers, reducing the number of recursive calls.

2. **Bottom-up DP (Tabulation)**:
   - Instead of recursion, we can compute Fibonacci numbers iteratively, building from the base cases up to \( F(n) \), storing intermediate results in a table (array).

### 1. Top-down (Memoization) Approach:

In the top-down approach, we start from \( n \) and recursively break it down into smaller subproblems. We use a cache to store the results of Fibonacci numbers already computed, preventing redundant calculations.

```python
def fib_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    # Base cases
    if n <= 1:
        return n
    
    # Check if the result is already in the cache
    if n in memo:
        return memo[n]

    # Recursive relation: F(n) = F(n-1) + F(n-2)
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    
    return memo[n]
```

### 2. Bottom-up (Tabulation) Approach:

In the bottom-up approach, we iteratively compute the Fibonacci numbers starting from the smallest values (base cases) and store them in an array or variables as we build up to \( F(n) \).

**Optimized Bottom-up DP (Tabulation):**
Instead of keeping an entire array of results, we only need to store the last two Fibonacci numbers at each step to compute the next one. This reduces the space complexity to \( O(1) \).

```python
def fib_bottom_up(n: int) -> int:
    if n <= 1:
        return n
    
    # Two variables to store the previous two Fibonacci numbers
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1
```

### Explanation:
- **Base cases**: \( F(0) = 0 \) and \( F(1) = 1 \) are handled separately.
- We iterate from \( i = 2 \) to \( n \) and use two variables `prev1` (for \( F(n-1) \)) and `prev2` (for \( F(n-2) \)) to compute \( F(n) \) as \( prev1 + prev2 \).
- After each step, we update `prev2` and `prev1` to hold the current and previous Fibonacci numbers.

### Time and Space Complexity:
- **Time complexity**: \( O(n) \) because we compute Fibonacci numbers from 0 to \( n \) once.
- **Space complexity**:
  - **Top-down with memoization**: \( O(n) \) for the recursion stack and memo table.
  - **Bottom-up**: \( O(1) \) for the optimized version, since we only store two variables.

### Example:

For \( n = 6 \), the Fibonacci sequence looks like this:
```
F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, F(6) = 8
```
Thus, \( F(6) = 8 \).

Both approaches will return the same result but with different performance characteristics (space usage and recursion depth).


#### 0/1 KnapSack pattern

The **0/1 Knapsack Problem** is one of the most well-known problems that can be solved using **dynamic programming (DP)**. It involves determining the maximum value of items that can be included in a knapsack with a weight capacity, where each item can either be taken or left (0/1 choice for each item).

### Problem Statement:
Given:
- A set of `n` items, where each item has a weight \( w_i \) and a value \( v_i \).
- A knapsack with a maximum weight capacity `W`.

You need to determine the maximum value you can obtain by selecting a subset of items such that the total weight does not exceed `W`. Each item can either be included (1) or not included (0).

### DP Approach:
To solve the 0/1 Knapsack problem using dynamic programming, we can follow these steps:

1. **Define the state (DP array)**:
   Let `dp[i][w]` represent the maximum value that can be obtained by selecting items from the first `i` items with a total weight capacity `w`.

2. **Base case**:
   - When no items are available, the value is zero: `dp[0][w] = 0` for all `w`.
   - When the capacity of the knapsack is zero, the value is also zero: `dp[i][0] = 0` for all `i`.

3. **Recurrence relation**:
   For each item `i`, we have two choices:
   - **Exclude the item**: The value will be the same as the value without this item, i.e., `dp[i-1][w]`.
   - **Include the item**: The value will be the value of the current item plus the best value we can achieve with the remaining weight capacity, i.e., `dp[i-1][w - w_i] + v_i` (if the item can fit in the knapsack).

   Thus, the recurrence relation is:
   \[
   dp[i][w] = \max(dp[i-1][w], dp[i-1][w - w_i] + v_i) \text{ if } w_i \leq w
   \]
   If the current item's weight exceeds the current capacity `w`, the item cannot be included, so:
   \[
   dp[i][w] = dp[i-1][w] \text{ if } w_i > w
   \]

4. **Final answer**:
   The value `dp[n][W]` will give the maximum value we can obtain with `n` items and a knapsack of capacity `W`.

### Code Implementation:

```python
def knapsack(weights, values, W):
    n = len(weights)
    # Create a DP table with (n+1) rows for items and (W+1) columns for capacities
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:  # Can include this item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Cannot include this item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]  # The maximum value for n items and capacity W
```

### Explanation:
1. We initialize a 2D array `dp` where `dp[i][w]` stores the maximum value we can achieve with `i` items and weight capacity `w`.
2. We fill the DP table based on whether we can include the current item `i` in the knapsack or not, following the recurrence relation.
3. The result is stored in `dp[n][W]`, which contains the maximum value for the given capacity `W` using all `n` items.

### Example:

Let’s say we have the following items:
- Item 1: weight = 2, value = 3
- Item 2: weight = 3, value = 4
- Item 3: weight = 4, value = 5
- Item 4: weight = 5, value = 6
And the knapsack has a weight capacity of `W = 5`.

The table will look like this (for 4 items and capacity 5):

```
    |   0   1   2   3   4   5  (Weight capacity)
----------------------------------------------
0   |   0   0   0   0   0   0  (No items)
1   |   0   0   3   3   3   3  (Item 1)
2   |   0   0   3   4   4   7  (Item 2)
3   |   0   0   3   4   5   7  (Item 3)
4   |   0   0   3   4   5   7  (Item 4)
```

So, the maximum value we can carry in the knapsack with weight capacity 5 is **7**.

### Time and Space Complexity:
- **Time complexity**: \( O(n \times W) \), where `n` is the number of items and `W` is the weight capacity. We compute every value in the DP table once.
- **Space complexity**: \( O(n \times W) \), because we maintain a 2D array for `n` items and `W` weight capacities.

### Space Optimization (1D DP):
Since the current state `dp[i][w]` only depends on the previous row `dp[i-1][w]`, we can optimize space by only maintaining a single 1D array, updating values from right to left.

```python
def knapsack_optimized(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)  # Only need 1D array

    # Fill DP array
    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]
```

### Space Complexity (Optimized):
- **Time complexity**: \( O(n \times W) \).
- **Space complexity**: \( O(W) \) since we are using only a 1D array.

#### Unbounded KnapSack

The **Unbounded Knapsack** problem is a variation of the 0/1 knapsack problem, where you can take an unlimited number of each item (as opposed to at most one of each in the 0/1 knapsack). The goal is to maximize the total value without exceeding the weight capacity of the knapsack.

### Problem Statement:
Given:
- `n` items, each with a weight \( w_i \) and a value \( v_i \).
- A knapsack with a maximum weight capacity `W`.

You can take any number of each item (including multiple copies of the same item) to maximize the total value in the knapsack without exceeding the weight capacity `W`.

### DP Approach:
Dynamic programming can be used to solve the unbounded knapsack problem in a way similar to the 0/1 knapsack problem, but with a small difference:
- Since you can take an item multiple times, you don't need to restrict yourself to including or excluding an item once. You should consider the possibility of including the same item multiple times in your solution.

### Steps:

1. **Define the state (DP array)**:
   Let `dp[w]` represent the maximum value that can be achieved with a knapsack capacity `w`.

2. **Base case**:
   - `dp[0] = 0`, since if the capacity is 0, the maximum value is also 0 (no items can be taken).

3. **Recurrence relation**:
   For each item `i`, for each possible knapsack capacity `w`, we can either:
   - **Exclude the item**: The value will remain the same as it was for the previous capacity, i.e., `dp[w]`.
   - **Include the item**: The value will be the value of the current item plus the best value for the remaining capacity, i.e., `dp[w - w_i] + v_i`.

   Thus, the recurrence relation is:
   \[
   dp[w] = \max(dp[w], dp[w - w_i] + v_i) \quad \text{if } w_i \leq w
   \]
   This is different from the 0/1 knapsack problem in that we do not require separate states for each item. We update the DP array from left to right, considering the same item multiple times.

4. **Final answer**:
   The value `dp[W]` will contain the maximum value achievable with the full knapsack capacity `W`.

### Code Implementation:

```python
def unboundedKnapsack(weights, values, W):
    n = len(weights)
    # Create a DP array of size W + 1 to store the maximum value for each capacity
    dp = [0] * (W + 1)
    
    # Fill DP array
    for w in range(1, W + 1):  # for each capacity
        for i in range(n):  # check each item
            if weights[i] <= w:  # If the current item can fit in the knapsack
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]
```

### Explanation:
1. We initialize a 1D array `dp` where `dp[w]` stores the maximum value that can be achieved with weight capacity `w`.
2. For each possible capacity `w`, we check each item:
   - If the item can fit in the knapsack (i.e., its weight \( w_i \leq w \)), we check the maximum value that can be achieved by either including the item or not.
   - If we include the item, we look at `dp[w - w_i] + v_i`, meaning the value we can achieve by using this item and the best solution for the remaining weight \( w - w_i \).
3. The result is stored in `dp[W]`, which gives us the maximum value for the knapsack with capacity `W`.

### Example:

Let’s say we have the following items:
- Item 1: weight = 1, value = 1
- Item 2: weight = 3, value = 4
- Item 3: weight = 4, value = 5
And the knapsack has a weight capacity of `W = 7`.

The table will look like this (for 3 items and capacity 7):

```
    |   0   1   2   3   4   5   6   7  (Weight capacity)
------------------------------------------------------
    |   0   0   0   0   0   0   0   0  (Initial)
Item1|   0   1   2   3   4   5   6   7  (Multiple Item 1)
Item2|   0   1   2   4   5   6   8   9  (Including Item 2)
Item3|   0   1   2   4   5   6   8   9  (Including Item 3)
```

The maximum value for a knapsack of weight 7 is **9** (taking three items: one of weight 3 and two of weight 1).

### Time and Space Complexity:
- **Time complexity**: \( O(n \times W) \), where `n` is the number of items and `W` is the capacity. We compute every value in the DP table once.
- **Space complexity**: \( O(W) \), since we only need a 1D DP array of size `W + 1`.

### Comparison with 0/1 Knapsack:
In the **0/1 knapsack problem**, we consider each item only once, so the recurrence relation is slightly different. In the **unbounded knapsack problem**, we consider each item multiple times, allowing for repeated inclusion of items in the solution.

### Optimized Approach (Iterating over items first):

Instead of iterating over each weight for each item, we can iterate over the items first and then over each possible weight. This order ensures that each item can be considered multiple times within the loop for weights, which aligns with the unbounded nature of the problem.

```python
def unboundedKnapsack_optimized(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    
    # Iterate over each item first
    for i in range(n):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]
```

### Space and Time Complexity (Optimized):
- **Time complexity**: \( O(n \times W) \) — same as the basic approach.
- **Space complexity**: \( O(W) \) — only one 1D array is needed.

#### Longest Common Subsequence DP Pattern

The **Longest Common Subsequence (LCS)** problem is a classic dynamic programming problem. The goal is to find the longest subsequence that appears in both given sequences in the same relative order, though not necessarily consecutively.

### Problem Statement:
Given two strings `s1` and `s2`, find the length of their longest common subsequence. A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

### DP Approach:
Dynamic programming helps solve this problem by breaking it down into overlapping subproblems. We will use a 2D table to store the results of subproblems (substrings of both `s1` and `s2`), building up the solution to the overall problem.

### Steps:

1. **Define the state (DP table)**:
   Let `dp[i][j]` represent the length of the longest common subsequence of the first `i` characters of `s1` and the first `j` characters of `s2`.

2. **Base case**:
   - When either `i` or `j` is 0 (i.e., when one of the strings is empty), the LCS length is 0: 
     \[
     dp[0][j] = dp[i][0] = 0
     \]

3. **Recurrence relation**:
   For each character `s1[i-1]` and `s2[j-1]`:
   - **If the characters match**: If `s1[i-1] == s2[j-1]`, then we can include this character in the LCS and increment the result by 1:
     \[
     dp[i][j] = dp[i-1][j-1] + 1
     \]
   - **If the characters don't match**: We can't include this character in the LCS, so the LCS length will be the maximum of the previous results:
     \[
     dp[i][j] = \max(dp[i-1][j], dp[i][j-1])
     \]

4. **Final answer**:
   The value `dp[len(s1)][len(s2)]` will contain the length of the longest common subsequence between `s1` and `s2`.

### Code Implementation:

```python
def longestCommonSubsequence(s1: str, s2: str) -> int:
    # Lengths of the strings
    n, m = len(s1), len(s2)
    
    # Create a DP table with (n+1) rows and (m+1) columns
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The last cell contains the length of the LCS
    return dp[n][m]
```

### Explanation:
1. **Initialization**: The DP table `dp[i][j]` is initialized with zeros, where each `dp[i][j]` will store the LCS length of `s1[:i]` and `s2[:j]`.
2. **Filling the DP Table**:
   - We iterate through both strings.
   - For each pair of characters `s1[i-1]` and `s2[j-1]`, we check if they match. If they do, we add 1 to the result from the previous subsequence (top-left diagonal cell), indicating that the current character extends the subsequence.
   - If they don’t match, we take the maximum value from the previous state (either ignoring one character from `s1` or ignoring one from `s2`).
3. **Final Result**: The value at `dp[len(s1)][len(s2)]` contains the length of the LCS of the entire strings `s1` and `s2`.

### Example:

Let’s find the LCS of two strings:
- `s1 = "abcde"`
- `s2 = "ace"`

```
    |   0   a   c   e
---------------------
  0 |   0   0   0   0
  a |   0   1   1   1
  b |   0   1   1   1
  c |   0   1   2   2
  d |   0   1   2   2
  e |   0   1   2   3
```

The length of the LCS is **3** (`ace`).

### Time and Space Complexity:
- **Time complexity**: \( O(n \times m) \), where `n` is the length of `s1` and `m` is the length of `s2`. We compute each entry of the DP table once.
- **Space complexity**: \( O(n \times m) \), as we need a 2D DP table to store the LCS lengths.

### Space Optimization:
The DP array can be optimized to a 1D array, since at any point, we only need the current row and the previous row. We can maintain two 1D arrays instead of the full 2D table.

```python
def longestCommonSubsequence_optimized(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    
    # Create two 1D DP arrays
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                curr[j] = prev[j - 1] + 1
            else:  # Characters don't match
                curr[j] = max(prev[j], curr[j - 1])
        # Move to the next row, make current the previous
        prev = curr[:]
    
    return prev[m]
```

### Space and Time Complexity (Optimized):
- **Time complexity**: \( O(n \times m) \).
- **Space complexity**: \( O(m) \), as we only store two rows (each of size `m + 1`).

### LCS Recovery:
If you want to recover the actual LCS string, you can backtrack through the DP table starting from `dp[n][m]` and reconstruct the sequence by following the matches (i.e., where `s1[i-1] == s2[j-1]`).

```python
def lcs_string(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Recover the LCS by backtracking
    i, j = n, m
    lcs = []
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:  # If there's a match, it's part of the LCS
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))
```

### Example:

For `s1 = "abcde"` and `s2 = "ace"`, the recovered LCS is `"ace"`.

---

This is the typical **DP pattern** used to solve the **LCS** problem efficiently.

#### Palindromes in DP

Palindromes are a popular topic in dynamic programming (DP) problems. Below are two well-known problems involving palindromes that are often solved using DP:

1. **Longest Palindromic Subsequence (LPS)**
2. **Longest Palindromic Substring (LPSstr)**

Let's break them down and see how DP can be applied in each case.

---

### 1. **Longest Palindromic Subsequence (LPS) Problem**

#### Problem Statement:
Given a string `s`, find the length of the longest subsequence of `s` that is a palindrome.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

#### DP Approach:

1. **Define the state (DP table)**:
   Let `dp[i][j]` represent the length of the longest palindromic subsequence in the substring `s[i:j+1]`.

2. **Base case**:
   - A single character is always a palindrome, so for every `i`, `dp[i][i] = 1`.

3. **Recurrence relation**:
   - If the characters `s[i] == s[j]`, the longest palindromic subsequence in the substring `s[i:j+1]` includes both these characters plus the LPS in the substring `s[i+1:j-1]`:
     \[
     dp[i][j] = dp[i+1][j-1] + 2
     \]
   - If `s[i] != s[j]`, then the LPS in `s[i:j+1]` is the maximum of either excluding the character at `i` or excluding the character at `j`:
     \[
     dp[i][j] = \max(dp[i+1][j], dp[i][j-1])
     \]

4. **Final answer**:
   The value `dp[0][n-1]` will give the length of the longest palindromic subsequence for the full string `s`, where `n` is the length of `s`.

#### Code Implementation:

```python
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    
    # Create a DP table
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the table for substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]
```

### Example:
For the string `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"`, and the length is **4**.

### Time and Space Complexity:
- **Time complexity**: \( O(n^2) \), where `n` is the length of the string.
- **Space complexity**: \( O(n^2) \) because we use a 2D DP table of size \( n \times n \).

---

### 2. **Longest Palindromic Substring (LPSstr) Problem**

#### Problem Statement:
Given a string `s`, find the longest substring of `s` that is a palindrome.

A **substring** is a contiguous sequence of characters within a string.

#### DP Approach:

1. **Define the state (DP table)**:
   Let `dp[i][j]` represent whether the substring `s[i:j+1]` is a palindrome (true or false).

2. **Base case**:
   - Every single character is a palindrome, so for every `i`, `dp[i][i] = True`.
   - For two-character substrings, if `s[i] == s[i+1]`, then `dp[i][i+1] = True`.

3. **Recurrence relation**:
   - For a substring `s[i:j+1]` of length greater than 2, if `s[i] == s[j]` and `dp[i+1][j-1]` is true, then `dp[i][j] = True`.

4. **Track the longest palindrome**:
   - Keep track of the start and length of the longest palindrome seen so far.

5. **Final answer**:
   You can return the substring `s[start:start + max_len]` where `start` is the beginning index of the longest palindrome and `max_len` is its length.

#### Code Implementation:

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    
    # Base case for empty string
    if n == 0:
        return ""
    
    # Create a DP table
    dp = [[False] * n for _ in range(n)]
    
    # Variables to track the start and maximum length of the longest palindrome
    start, max_len = 0, 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for two-character palindromes
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]
```

### Example:
For the string `s = "babad"`, the longest palindromic substring is either `"bab"` or `"aba"`, and the length is **3**.

### Time and Space Complexity:
- **Time complexity**: \( O(n^2) \), where `n` is the length of the string.
- **Space complexity**: \( O(n^2) \) due to the use of the 2D DP table.

---

### Optimized Solution for Longest Palindromic Substring (Expand Around Center):

Although the DP solution works well, there's a more efficient solution to solve the **Longest Palindromic Substring** problem with \( O(n^2) \) time complexity and \( O(1) \) space complexity using the **Expand Around Center** technique.

#### Explanation:
A palindrome mirrors around its center, so for each character (or pair of characters), treat it as the center and expand outward while the characters on both sides are the same.

#### Code Implementation:

```python
def longestPalindromeExpand(s: str) -> str:
    if not s or len(s) == 0:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        # Expand around a single character (odd-length palindromes)
        len1 = expandAroundCenter(s, i, i)
        # Expand around two characters (even-length palindromes)
        len2 = expandAroundCenter(s, i, i + 1)
        
        # Get the maximum length from both expansions
        max_len = max(len1, len2)
        
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

def expandAroundCenter(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
```

### Time and Space Complexity:
- **Time complexity**: \( O(n^2) \), where `n` is the length of the string.
- **Space complexity**: \( O(1) \), since we are not using any extra space except for variables.

### Summary of Problems:
1. **Longest Palindromic Subsequence (LPS)**: Use a 2D DP table to track the longest subsequences.
2. **Longest Palindromic Substring (LPSstr)**: Can be solved using a 2D DP table or an optimized **Expand Around Center** approach.


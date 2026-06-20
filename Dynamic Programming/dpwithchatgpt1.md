Absolutely. DP is one of those topics where people suffer because they try to **memorize solutions**. We’ll do the opposite: learn the **design system** behind DP, then map questions into patterns.

I checked current high-quality resources: LeetCode’s official DP study plan is built around “10 Essential DP Patterns” and recursive learning, MIT 6.006 teaches DP starting from recursion/memoization, and USACO frames DP as breaking a problem into subproblems to avoid repeated brute-force computation. That matches exactly how we should train. ([LeetCode][1])

## The goal

After this, you should be able to look at a DP problem and say:

> “This is not random. The state is probably this, the choice is this, the recurrence is this, and the time complexity should be around this.”

For FAANG-level interviews, you do not need to solve every exotic competitive-programming DP. You need mastery over interview-heavy patterns: 1D DP, 2D DP, knapsack, subsequence DP, interval DP, state-machine DP, tree DP, and bitmask DP.

---

# 1. The core DP design framework

Every DP problem has six pieces:

## 1. State

What information uniquely defines a subproblem?

Examples:

```text
dp[i]             -> answer up to index i
dp[i][j]          -> answer using first i of string1 and first j of string2
dp[l][r]          -> answer for subarray/string from l to r
dp[i][target]     -> answer after considering i items with remaining target
dp[node][take]    -> answer in a tree depending on whether node is taken
dp[mask]          -> answer for a subset of chosen items
```

## 2. Choice

At this state, what decision do I make?

Examples:

```text
Take or skip?
Move right or down?
Match characters or not?
Buy, sell, hold, cooldown?
Cut at position k?
Pick current element as part of subsequence?
```

## 3. Recurrence

How do choices connect to smaller states?

Example:

```python
dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
```

This is House Robber logic: either skip current house, or rob it and jump two steps back.

## 4. Base case

Where does recursion stop?

Examples:

```text
i == n
target == 0
l > r
i == 0 or j == 0
node == null
```

## 5. Evaluation order

Can we compute top-down with memoization, or bottom-up?

For interviews, start with:

```python
dfs(...) + cache
```

Then convert to tabulation only when needed.

## 6. Answer location

Where is the final answer?

Examples:

```text
dp[n]
dp[0]
dp[n][m]
max(dp[i])
dp[0][n-1]
```

---

# 2. My DP attack template

Use this for almost every DP problem:

```python
from functools import cache

def solve(...):
    @cache
    def dp(state):
        if base_case:
            return base_value

        ans = initial_value

        for choice in choices:
            ans = combine(ans, dp(next_state) + cost)

        return ans

    return dp(start_state)
```

Then ask:

```text
What changes?       -> state
What can I do?      -> choices
What is smaller?    -> transition
What is impossible? -> invalid state
What do I optimize? -> min / max / count / true-false
```

This is the entire game.

---

# 3. How to recognize DP

A problem is likely DP when you see:

```text
minimum / maximum / number of ways / possible or not
```

combined with:

```text
choices at every step
overlapping subproblems
constraints not large enough for greedy brute force
```

Constraint hints are very important:

| Constraint                    | Usual DP Shape                    |
| ----------------------------- | --------------------------------- |
| n up to 100000                | O(n), O(n log n), optimized 1D DP |
| n up to 1000                  | O(n²) DP possible                 |
| n up to 300–500               | O(n³) interval DP possible        |
| n up to 20                    | Bitmask DP possible               |
| target/sum up to 10000        | Knapsack/subset-sum DP possible   |
| two strings length up to 1000 | 2D string DP possible             |

---

# 4. The pattern map

## Pattern 1: Fibonacci / linear DP

Use when the answer at index `i` depends on previous few indices.

State:

```text
dp[i] = answer up to i
```

Questions:

```text
Climbing Stairs
Min Cost Climbing Stairs
House Robber
Decode Ways
Delete and Earn
```

Core recurrence style:

```python
dp[i] = f(dp[i - 1], dp[i - 2])
```

Start here because it teaches the DP muscle without too many dimensions.

---

## Pattern 2: Take / skip DP

Use when each element can be included or excluded.

State:

```text
dp[i] = best answer from index i onward
```

Choice:

```text
take current
skip current
```

Questions:

```text
House Robber
House Robber II
Partition Equal Subset Sum
Target Sum
Ones and Zeroes
```

Example:

```python
dp(i) = max(
    dp(i + 1),              # skip
    nums[i] + dp(i + 2)     # take
)
```

---

## Pattern 3: Grid DP

Use when moving through a matrix.

State:

```text
dp[r][c] = answer to reach cell r, c
```

Questions:

```text
Unique Paths
Unique Paths II
Minimum Path Sum
Dungeon Game
Maximal Square
Cherry Pickup
```

Core recurrence:

```python
dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
```

---

## Pattern 4: Knapsack DP

Use when there is a capacity, target, sum, or limited resource.

USACO’s knapsack guide describes these problems as choosing/filling items under a limited container/capacity, with state usually tracking capacity and transitions trying to add an item. ([usaco.guide][2])

State:

```text
dp[i][capacity] = best answer using first i items
```

Questions:

```text
0/1 Knapsack
Partition Equal Subset Sum
Target Sum
Last Stone Weight II
Ones and Zeroes
```

The most important distinction:

```text
0/1 knapsack: each item once
unbounded knapsack: item can be reused
```

---

## Pattern 5: Coin change / unbounded knapsack

Use when you can reuse choices.

Questions:

```text
Coin Change
Coin Change II
Combination Sum IV
Perfect Squares
```

Important interview trap:

```text
Coin Change I     -> minimum coins
Coin Change II    -> number of combinations
Combination Sum IV -> number of ordered sequences
```

Order matters a lot.

---

## Pattern 6: Subsequence DP

Use when you compare strings or arrays and can skip characters.

State:

```text
dp[i][j] = answer using s1[:i] and s2[:j]
```

Questions:

```text
Longest Common Subsequence
Edit Distance
Distinct Subsequences
Interleaving String
Delete Operation for Two Strings
Regular Expression Matching
Wildcard Matching
```

MIT’s 6.006 lecture notes specifically include DP lectures covering LCS, LIS, and coin problems, which are exactly the foundation for this category. ([MIT OpenCourseWare][3])

---

## Pattern 7: LIS-style DP

Use when you need an increasing/decreasing subsequence or ordering chain.

Questions:

```text
Longest Increasing Subsequence
Number of LIS
Russian Doll Envelopes
Largest Divisible Subset
Best Team With No Conflicts
```

Two versions matter:

```text
O(n²) DP version      -> easier to derive
O(n log n) binary search version -> optimized interview version
```

Learn both, but understand DP first.

---

## Pattern 8: Palindrome DP

Use when substrings matter and both ends interact.

State:

```text
dp[l][r] = answer for substring s[l:r+1]
```

Questions:

```text
Palindromic Substrings
Longest Palindromic Subsequence
Minimum Insertion Steps to Make a String Palindrome
Palindrome Partitioning II
```

Typical recurrence:

```python
if s[l] == s[r]:
    dp[l][r] = 2 + dp[l + 1][r - 1]
else:
    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
```

---

## Pattern 9: Interval DP

Use when you split a range into two smaller ranges.

USACO describes range DP as useful when answers for subarrays can be combined independently, often by trying a split point and processing subarrays in increasing length. It also notes the common O(n³) shape. ([usaco.guide][4])

State:

```text
dp[l][r] = best answer for interval l...r
```

Questions:

```text
Burst Balloons
Minimum Cost to Cut a Stick
Stone Game variants
Matrix Chain Multiplication
Palindrome partition variants
```

Core recurrence:

```python
for k in range(l, r + 1):
    dp[l][r] = best(dp[l][r], dp[l][k] + dp[k + 1][r] + cost)
```

This is where many FAANG-hard DP questions live.

---

## Pattern 10: State machine DP

Use when the problem has modes: holding stock, not holding, cooldown, transaction count, etc.

State:

```text
dp[day][holding][transactions]
```

Questions:

```text
Best Time to Buy and Sell Stock I
Stock II
Stock III
Stock IV
Stock with Cooldown
Stock with Transaction Fee
Paint House
Paint Fence
```

This pattern looks scary, but it is very mechanical.

Example states:

```text
hold[i] = max profit on day i while holding stock
cash[i] = max profit on day i while not holding stock
```

---

## Pattern 11: Tree DP

Use when choices at a node affect children.

State:

```text
dp(node) = answer for subtree
```

Sometimes:

```text
dp(node, taken)
```

Questions:

```text
House Robber III
Binary Tree Maximum Path Sum
Diameter of Binary Tree
Binary Tree Cameras
Maximum Sum BST in Binary Tree
```

Tree DP is basically recursion + “what do I return to parent?”

---

## Pattern 12: Bitmask DP

Use when `n <= 20` and the state is a subset.

State:

```text
dp[mask] = best answer after choosing this subset
```

USACO’s bitmask DP section focuses on representing sets using bitmasks, which is the key technique behind subset-state DP. ([usaco.guide][5])

Questions:

```text
Can I Win
Partition to K Equal Sum Subsets
Stickers to Spell Word
Shortest Path Visiting All Nodes
Travelling Salesman-style problems
```

This is usually advanced interview DP, but worth learning after the basics.

---

# 5. The question ladder I want you to follow

NeetCode 150 currently separates 1-D Dynamic Programming and 2-D Dynamic Programming as explicit categories, and its list includes classic DP problems like Climbing Stairs, House Robber, Decode Ways, Coin Change, LIS, Partition Equal Subset Sum, Unique Paths, LCS, Word Break, Edit Distance, Maximal Square, and Burst Balloons. ([NeetCode][6])

## Level 1: DP foundation

Do these first:

```text
70. Climbing Stairs
746. Min Cost Climbing Stairs
198. House Robber
213. House Robber II
91. Decode Ways
53. Maximum Subarray
152. Maximum Product Subarray
```

Goal: identify `dp[i]`.

---

## Level 2: Grid and 2D basics

```text
62. Unique Paths
63. Unique Paths II
64. Minimum Path Sum
221. Maximal Square
120. Triangle
```

Goal: become comfortable with `dp[r][c]`.

---

## Level 3: Knapsack and target DP

```text
416. Partition Equal Subset Sum
494. Target Sum
322. Coin Change
518. Coin Change II
377. Combination Sum IV
279. Perfect Squares
1049. Last Stone Weight II
474. Ones and Zeroes
```

Goal: understand target/capacity state.

---

## Level 4: String DP

```text
1143. Longest Common Subsequence
72. Edit Distance
115. Distinct Subsequences
139. Word Break
97. Interleaving String
10. Regular Expression Matching
44. Wildcard Matching
```

Goal: master `dp[i][j]`.

---

## Level 5: LIS and subsequence chain DP

```text
300. Longest Increasing Subsequence
673. Number of Longest Increasing Subsequence
354. Russian Doll Envelopes
368. Largest Divisible Subset
1626. Best Team With No Conflicts
```

Goal: understand “previous compatible element” transitions.

---

## Level 6: Palindrome and interval DP

```text
647. Palindromic Substrings
516. Longest Palindromic Subsequence
1312. Minimum Insertion Steps to Make a String Palindrome
132. Palindrome Partitioning II
312. Burst Balloons
1547. Minimum Cost to Cut a Stick
1039. Minimum Score Triangulation of Polygon
```

Goal: learn `dp[l][r]`.

---

## Level 7: State machine DP

```text
121. Best Time to Buy and Sell Stock
122. Stock II
123. Stock III
188. Stock IV
309. Stock with Cooldown
714. Stock with Transaction Fee
256/265. Paint House variants
```

Goal: model modes clearly.

---

## Level 8: Tree and bitmask DP

```text
337. House Robber III
124. Binary Tree Maximum Path Sum
968. Binary Tree Cameras
464. Can I Win
698. Partition to K Equal Sum Subsets
691. Stickers to Spell Word
847. Shortest Path Visiting All Nodes
```

Goal: handle recursive structures and subset states.

---

# 6. Eight-week training plan

## Weeks 1–2: DP fundamentals

Focus:

```text
recursion
memoization
1D DP
take/skip
grid DP
```

Target: 20–25 problems.

Rule: For every problem, write top-down first.

---

## Weeks 3–4: Knapsack and string DP

Focus:

```text
target sum
coin change
0/1 vs unbounded knapsack
LCS
Edit Distance
Word Break
```

Target: 25–30 problems.

This is the most important phase for FAANG-style medium questions.

---

## Weeks 5–6: Palindrome, LIS, interval DP

Focus:

```text
LIS O(n²)
LIS O(n log n)
palindrome substring/subsequence
Burst Balloons
Cut Stick
```

Target: 20–25 problems.

This is where you move from “I know DP” to “I can handle hard DP.”

---

## Week 7: State machine, tree, bitmask

Focus:

```text
stock DP
tree DP
small-n bitmask DP
```

Target: 15–20 problems.

---

## Week 8: Mixed FAANG simulation

Daily routine:

```text
1 known-pattern medium
1 unknown-pattern medium
1 hard every 2 days
```

For each problem, force yourself to classify the pattern before coding.

---

# 7. The practice rule that will make you strong

For every DP problem, maintain this journal:

```text
Problem:
Pattern:
State:
Choice:
Recurrence:
Base case:
Answer:
Time:
Space:
Can space be optimized?
Similar problems:
Mistake I made:
```

This is how you stop forgetting DP. You are not collecting solutions; you are collecting patterns.

---

# 8. First concept to internalize today

DP starts as brute force recursion.

Example: House Robber.

At every house:

```text
Option 1: skip it
Option 2: rob it, then skip the next one
```

Top-down:

```python
from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0

            skip = dp(i + 1)
            take = nums[i] + dp(i + 2)

            return max(skip, take)

        return dp(0)
```

Now convert to bottom-up:

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]
```

Then optimize space:

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        next1 = 0  # dp[i + 1]
        next2 = 0  # dp[i + 2]

        for i in range(len(nums) - 1, -1, -1):
            curr = max(next1, nums[i] + next2)
            next2 = next1
            next1 = curr

        return next1
```

This is the learning path for almost every DP problem:

```text
brute force recursion -> memoization -> tabulation -> space optimization
```

---

# 9. Your FAANG-readiness benchmark

You are DP-ready when:

```text
Easy DP: under 10 minutes
Standard medium DP: 20–35 minutes
Hard familiar-pattern DP: 45–60 minutes
Unknown DP: can identify state + recurrence even if coding takes longer
```

Before interviews, I would want you to solve around:

```text
30 foundation DP
25 knapsack/string DP
20 palindrome/interval/LIS DP
15 state-machine/tree/bitmask DP
```

That is roughly 90 serious DP problems, with revision. Not 300 random ones.

---

# 10. How we should proceed from here

We should go pattern by pattern. I’ll teach each pattern like this:

```text
1. Explain the intuition
2. Show how to identify it
3. Derive recurrence from brute force
4. Solve 2–3 examples
5. Give you practice problems
6. Review your solution style
7. Teach optimization
```

Start with this order:

```text
Module 1: 1D DP + take/skip
Module 2: Grid DP
Module 3: Knapsack
Module 4: String DP
Module 5: LIS
Module 6: Palindrome DP
Module 7: Interval DP
Module 8: State-machine DP
Module 9: Tree DP
Module 10: Bitmask DP
```

For the next session, I’d start you with **Module 1: 1D DP and take/skip**, covering:

```text
Climbing Stairs
Min Cost Climbing Stairs
House Robber
House Robber II
Decode Ways
Delete and Earn
```

That will build the base correctly before we touch harder patterns.

[1]: https://leetcode.com/studyplan/dynamic-programming/ "Dynamic Programming - Study Plan - LeetCode"
[2]: https://usaco.guide/gold/knapsack "Knapsack DP · USACO Guide"
[3]: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/ "Lecture Notes | Introduction to Algorithms | Electrical Engineering and Computer Science | MIT OpenCourseWare"
[4]: https://usaco.guide/gold/dp-ranges "Range DP · USACO Guide"
[5]: https://usaco.guide/gold/dp-bitmasks?utm_source=chatgpt.com "Bitmask DP"
[6]: https://neetcode.io/practice/practice/neetcode150 "NeetCode 150 - Coding Interview Questions"

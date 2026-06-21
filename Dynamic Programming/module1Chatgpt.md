Perfect. **Module 1 = 1D DP + Take/Skip DP.**

This is the foundation. A lot of later DP patterns are just this idea with more dimensions.

LeetCode and NeetCode both place problems like **Climbing Stairs**, **Min Cost Climbing Stairs**, **House Robber**, **House Robber II**, **Decode Ways**, and related problems in the 1D DP bucket, so this is the right starting point. ([LeetCode][1])

---

# Module 1: 1D DP Mental Model

In 1D DP, your state is usually one of these:

```text
dp[i] = answer up to index i
```

or

```text
dp[i] = answer starting from index i
```

That’s it.

Most beginners get confused because they do not decide clearly whether `dp[i]` means:

```text
past-based: answer until i
future-based: answer from i onward
```

Both are fine. But you must be consistent.

---

# The universal 1D DP question

For every 1D DP problem, ask:

```text
At index i, what are my choices?
```

Usually the choices are:

```text
move 1 step
move 2 steps
take current
skip current
decode 1 digit
decode 2 digits
rob current
skip current
```

Then the recurrence becomes obvious.

---

# Pattern A: Climbing / Fibonacci DP

Use this when the problem says:

```text
You can move 1 or 2 steps.
How many ways?
Minimum cost?
Reach the end?
```

## Problem 1: Climbing Stairs

The problem: you have `n` stairs, and each move can be either 1 step or 2 steps. Return the number of distinct ways to reach the top. ([NeetCode][2])

### Thought process

To reach stair `n`, your last move was either:

```text
from n - 1 using 1 step
from n - 2 using 2 steps
```

So:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

Base cases:

```text
ways(1) = 1
ways(2) = 2
```

This is Fibonacci-style DP.

---

## Top-down version

```python
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i: int) -> int:
            if i == n:
                return 1

            if i > n:
                return 0

            one_step = dp(i + 1)
            two_steps = dp(i + 2)

            return one_step + two_steps

        return dp(0)
```

Here:

```text
dp(i) = number of ways to reach top from stair i
```

This is often the easiest way to design DP.

---

## Bottom-up version

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
```

Here:

```text
dp[i] = number of ways to reach stair i
```

---

## Space optimized version

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

---

# Pattern B: Minimum Cost DP

Now instead of “how many ways,” the question asks “minimum cost.”

## Problem 2: Min Cost Climbing Stairs

You are given `cost[i]`, the cost of stepping on stair `i`. After paying the cost, you can climb either 1 or 2 steps. You may start from index `0` or index `1`, and you need the minimum cost to reach the top. ([LeetCode][1])

### Thought process

At stair `i`, you pay `cost[i]`.

Then you choose:

```text
go to i + 1
go to i + 2
```

So:

```text
dp(i) = cost[i] + min(dp(i + 1), dp(i + 2))
```

Base case:

```text
if i >= n:
    return 0
```

Because once you cross the last stair, you are already at the top.

---

## Top-down version

```python
from functools import cache
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0

            return cost[i] + min(dp(i + 1), dp(i + 2))

        return min(dp(0), dp(1))
```

Here:

```text
dp(i) = minimum cost to reach the top starting from stair i
```

The final answer is:

```text
min(dp(0), dp(1))
```

because the problem allows you to start at stair `0` or stair `1`.

---

## Bottom-up version

```python
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])
```

---

## Space optimized version

```python
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1 = 0
        next2 = 0

        for i in range(len(cost) - 1, -1, -1):
            curr = cost[i] + min(next1, next2)
            next2 = next1
            next1 = curr

        return min(next1, next2)
```

But this version is a little easier to get wrong mentally. For interviews, the `dp` array version is completely acceptable.

---

# Pattern C: Take / Skip DP

This is one of the most important DP patterns.

Use it when the problem says:

```text
You may choose some elements.
There is a restriction.
Find max/min/count.
```

The core idea:

```text
At index i:
1. skip current
2. take current
```

So most recurrences look like this:

```text
dp(i) = best(skip, take)
```

---

# Problem 3: House Robber

You are given money in houses arranged in a line. You cannot rob two adjacent houses. Return the maximum money you can rob. ([NeetCode][3])

### Thought process

At house `i`, you have two choices:

```text
skip house i  -> dp(i + 1)
rob house i   -> nums[i] + dp(i + 2)
```

Why `i + 2` after robbing?

Because if you rob house `i`, you cannot rob house `i + 1`.

So:

```text
dp(i) = max(dp(i + 1), nums[i] + dp(i + 2))
```

---

## Top-down version

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

This is the cleanest interview explanation.

---

## Bottom-up version

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            skip = dp[i + 1]
            take = nums[i] + dp[i + 2]
            dp[i] = max(skip, take)

        return dp[0]
```

---

## Space optimized version

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

Complexity:

```text
Time: O(n)
Space: O(1)
```

---

# Very important: two DP directions

House Robber can also be written as:

```text
dp[i] = max money from houses 0...i
```

Then:

```text
dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
```

Code:

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            curr = max(prev1, money + prev2)
            prev2 = prev1
            prev1 = curr

        return prev1
```

Both versions are correct.

But for learning, I recommend this style first:

```text
dp(i) = answer from index i onward
```

because it maps naturally to recursion.

---

# Pattern D: Circular Take / Skip

## Problem 4: House Robber II

Now houses are arranged in a circle.

That means:

```text
house 0 and house n - 1 are adjacent
```

So you cannot take both.

The trick is to split the problem into two normal House Robber problems:

```text
Case 1: rob from houses 0 to n - 2
Case 2: rob from houses 1 to n - 1
```

Then answer:

```text
max(case1, case2)
```

Code:

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            prev2 = 0
            prev1 = 0

            for money in arr:
                curr = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = curr

            return prev1

        skip_last = rob_linear(nums[:-1])
        skip_first = rob_linear(nums[1:])

        return max(skip_last, skip_first)
```

This is a very common interview move:

```text
Circular constraint -> break into two linear cases
```

---

# Pattern E: Decode Ways DP

This is still 1D DP, but it feels harder because of validation.

## Problem 5: Decode Ways

Digits map to letters:

```text
1 -> A
2 -> B
...
26 -> Z
```

You need to count how many valid decodings exist.

Example:

```text
"12"
```

Can be:

```text
"1" + "2" -> A B
"12"      -> L
```

Answer:

```text
2
```

---

## Thought process

At index `i`, you can:

```text
decode one digit if s[i] is not '0'
decode two digits if s[i:i+2] is between 10 and 26
```

So:

```text
dp(i) = ways from index i
```

Choices:

```text
one digit  -> dp(i + 1)
two digits -> dp(i + 2)
```

---

## Code

```python
from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i: int) -> int:
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            ways = dp(i + 1)

            if i + 1 < n:
                two_digit = int(s[i:i + 2])
                if 10 <= two_digit <= 26:
                    ways += dp(i + 2)

            return ways

        return dp(0)
```

This is the same as Climbing Stairs, but with conditions.

Climbing Stairs:

```text
always allowed to take 1 step
always allowed to take 2 steps
```

Decode Ways:

```text
1-digit move allowed only if s[i] != '0'
2-digit move allowed only if 10 <= value <= 26
```

That is the whole insight.

---

# Your Module 1 DP template

Use this for almost every first attempt:

```python
from functools import cache

def solve(arr):
    n = len(arr)

    @cache
    def dp(i):
        if i >= n:
            return 0

        # choices
        option1 = dp(i + 1)
        option2 = arr[i] + dp(i + 2)

        return max(option1, option2)

    return dp(0)
```

Then modify:

```text
max       -> when asking best/profit/largest
min       -> when asking minimum cost
sum       -> when asking number of ways
boolean   -> when asking possible or not
```

---

# How to identify the recurrence

Use this table:

| Problem type    | State                            | Choices                | Recurrence style                     |
| --------------- | -------------------------------- | ---------------------- | ------------------------------------ |
| Climbing Stairs | `dp(i)` ways from stair `i`      | 1 step / 2 steps       | `dp(i+1) + dp(i+2)`                  |
| Min Cost Stairs | `dp(i)` min cost from stair `i`  | 1 step / 2 steps       | `cost[i] + min(...)`                 |
| House Robber    | `dp(i)` max money from house `i` | skip / rob             | `max(dp(i+1), nums[i] + dp(i+2))`    |
| House Robber II | linear robbery on two ranges     | skip first / skip last | `max(rob(nums[:-1]), rob(nums[1:]))` |
| Decode Ways     | `dp(i)` ways from char `i`       | 1 digit / 2 digits     | conditional sum                      |

---

# Practice Set for Module 1

Do these in this exact order:

## Easy warm-up

```text
1. LeetCode 70 - Climbing Stairs
2. LeetCode 746 - Min Cost Climbing Stairs
3. LeetCode 1137 - N-th Tribonacci Number
```

## Core take/skip

```text
4. LeetCode 198 - House Robber
5. LeetCode 213 - House Robber II
6. LeetCode 740 - Delete and Earn
```

## Counting ways

```text
7. LeetCode 91 - Decode Ways
8. LeetCode 639 - Decode Ways II, optional hard later
```

## Kadane-style 1D DP

```text
9. LeetCode 53 - Maximum Subarray
10. LeetCode 152 - Maximum Product Subarray
```

NeetCode’s 1D DP resources also group several of these together, including Climbing Stairs, Min Cost Climbing Stairs, House Robber, House Robber II, Decode Ways, Maximum Product Subarray, Word Break, LIS, and Partition Equal Subset Sum. ([GitHub][4])

---

# Your homework for today

Solve these four first:

```text
70. Climbing Stairs
746. Min Cost Climbing Stairs
198. House Robber
213. House Robber II
```

For each problem, write this before coding:

```text
State:
Choice:
Recurrence:
Base case:
Answer:
Time:
Space:
```

Example for House Robber:

```text
State:
dp(i) = maximum money I can rob starting from house i

Choice:
skip house i or rob house i

Recurrence:
dp(i) = max(dp(i + 1), nums[i] + dp(i + 2))

Base case:
if i >= n: return 0

Answer:
dp(0)

Time:
O(n)

Space:
O(n) with memo, O(1) if optimized
```

---

# Mini test before you code

Answer these mentally:

### 1. In Climbing Stairs, why is it addition?

Because we are counting **all possible ways**.

```text
dp(i) = dp(i + 1) + dp(i + 2)
```

### 2. In Min Cost Climbing Stairs, why is it minimum?

Because we need the **cheapest path**.

```text
dp(i) = cost[i] + min(dp(i + 1), dp(i + 2))
```

### 3. In House Robber, why is it maximum?

Because we need the **largest money**.

```text
dp(i) = max(dp(i + 1), nums[i] + dp(i + 2))
```

### 4. In Decode Ways, why is it conditional addition?

Because we are counting ways, but only valid decodings are allowed.

```text
if one digit valid:
    ways += dp(i + 1)

if two digits valid:
    ways += dp(i + 2)
```

---

# The main lesson of Module 1

Most 1D DP is just this:

```text
At index i, try every valid choice.
Use recursion to solve the rest.
Cache repeated work.
```

Then optimize only after the recurrence is clear.

Your first target is not speed. Your first target is being able to say:

```text
This is my state.
These are my choices.
This is my recurrence.
```

Send me your solution for **Climbing Stairs** first, and I’ll review it like an interviewer.

[1]: https://leetcode.com/problems/min-cost-climbing-stairs/?utm_source=chatgpt.com "Min Cost Climbing Stairs"
[2]: https://neetcode.io/solutions/climbing-stairs?utm_source=chatgpt.com "70. Climbing Stairs - Solution & Explanation"
[3]: https://neetcode.io/problems/house-robber/question?utm_source=chatgpt.com "House Robber"
[4]: https://github.com/dipjul/NeetCode-150?utm_source=chatgpt.com "dipjul/NeetCode-150"

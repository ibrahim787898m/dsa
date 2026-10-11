# Sliding Window — Quiz: Lesson 2

## Q1

**There's a while loop inside a for loop, yet the time complexity is O(n), not O(n²). Explain why in your own words.**

1. q1. for example we will run for loop for n times so each time when we run for loop the while loop will run one time like 1st for loop -> while will run 1 times which is O(1) not n times. so for loop n times and each for loop while is O(1) -> n * O(1) -> O(n). thats why we get O(n) instead of O(n^2).
2. so the mistake that i made saying while loop runs each time per loop which is not correct because is some for loop while loop wont run or in some for loop while loop will run. the thing is that in entire run while loop will run n times that i said but could not give the proper reason which is in while loop left moves forward and start with 0 and go upto n which is exactly n times in entire run.

## Q2 (trace)

**Trace `min_len(7, [2, 3, 1, 2, 4, 3])`. At each step, show right, what's added, any shrinking (what's removed and the new left), the window sum, and best. Give the final answer.**

### First trace

```text
1st loop: left = 0 right = 0 -> window = 2 -> window < target -> best = -inf
2nd loop: left = 0 right = 1 -> window = 5 -> window < target -> best = -inf
3rd loop: left = 0 right = 2 -> window = 6 -> window < target -> best = -inf
4th loop: left = 0 right = 3 -> window = 8 -> window > target -> best = 4 -> window = 6 left = 1
5th loop: left = 1 right = 4 -> window = 10 -> window > target -> best = 4 -> window = 7 left = 2
6th loop: left = 2 right = 5 -> window = 10 -> window > target -> best = 4 -> window = 9 left = 3
best = 4
```

### Second trace

```python
def min_len(target, nums):
    left = 0
    window = 0
    best = float("inf")
    for right in range(len(nums)):
        window += nums[right]
        while window >= target:                # valid, so try to shrink it
            best = min(best, right - left + 1) # record BEFORE shrinking
            window -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
```

```text
1st loop: left = 0 right = 0 -> window = 2 -> window < target -> best = inf
2nd loop: left = 0 right = 1 -> window = 5 -> window < target -> best = inf
3rd loop: left = 0 right = 2 -> window = 6 -> window < target -> best = inf
4th loop: left = 0 right = 3 -> window = 8 -> window > target -> best = 4 -> window = 6 left = 1
5th loop: left = 1 right = 4 -> window = 10 -> window > target -> best = 4 -> window = 7 left = 2
    -> window = target -> best = 3 -> window = 6 left 3
6th loop: left = 3 right = 5 -> window = 9 -> window > target -> best = 3 -> window = 7 left = 4
    -> window = target -> best = 2 -> window = 3 left = 5
```

## Q3

**Why is the window length `right - left + 1` and not `right - left`? Give a general reason, not just one example (remember your Q3 feedback 😉).**

if we do right - left we will get the length between the left but we want length of substring from left to right and right like 2,4,3,6 right = 2 left = 0 2 - 0 = 2 which is not correct we are doing substitution with the index number and to get the length after the substitution we need to add 1 so the length will be 3.

## Q4

**Why does this pattern break with negative numbers? Construct a small array with a negative number where `longest_at_most` returns the wrong answer, and show what it returns compared with the correct answer.**

### First trace

```text
[3, 8, -2], 7
1st loop: left = 0 right = 0 -> window = 3 -> window < limit 7 -> best = 1
2nd loop: left = 0 right = 1 -> window = 11 -> window > limit 7 -> window = 5 left = 1 -> best = 1
3rd loop: left = 1 right = 2 -> window = 3 -> window < limit 7 -> best = 2
best = 2
```

### Second trace

```python
# [3, 8, -2], 7
def longest_at_most(nums, limit):
    left = 0
    window = 0
    best = 0
    for right in range(len(nums)):
        window += nums[right]              # 1. grow: add the new element
        while window > limit:              # 2. shrink while the window is INVALID
            window -= nums[left]
            left += 1
        best = max(best, right - left + 1) # 3. window is valid, so record it
    return best
```

```text
1st loop: left = 0 right = 0 -> window = 3 -> window < limit 7 -> best = 1
2nd loop: left = 0 right = 1 -> window = 11 -> window > limit 7 -> window = 8 left = 1 -> best = 1
    -> left = 1 right = 1 -> window = 0 left = 2 -> best = 1
3rd loop: left = 2 right = 2 -> window = -2 -> window < limit 7 -> best = 1
best = 1
correct answer is best = 2 -> [8, -2] = 6 < 7
```

## Q5 (code)

**LeetCode 1004, Max Consecutive Ones III: given a binary array nums (only 0s and 1s) and an integer k, return the maximum number of consecutive 1s if you can flip at most k zeros to 1.**

```text
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  →  6
```

**Hint:** rephrase it as "the longest window containing at most k zeros." Which flavor is that, and what do you track instead of a sum?

```python
left = 0
right = 0
count = 0
best = 0

for right in range(len(nums)):
    if nums[right] == 0:
        count += 1

    while count > k:
        left += 1

    best = max(best, right - left + 1)
```

```text
1st loop: left = 0 right = 0 -> count = 0 < k -> best = 1
2nd loop: left = 0 right = 1 -> count = 0 < k -> best = 2
3rd loop: left = 0 right = 2 -> count = 0 < k -> best = 3
4th loop: left = 0 right = 3 -> count = 1 < k -> best = 4
5th loop: left = 0 right = 4 -> count = 2 = k -> best = 5
6th loop: left = 0 right = 5 -> count = 3 > k
                -> left = 1 -> best = 5
```

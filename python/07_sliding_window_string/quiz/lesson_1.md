# Sliding Window — Quiz: Lesson 1

## Q1

**What's the time complexity of the brute force and of the sliding window version? In one sentence, explain why the sliding window version is faster.**

in brute force we are forcing to get the 1st 3 element sum than in second loop we are doing same forcing next 3 element to get the sum and this thing is repeating and each time we are adding 2 element that we already added in previous lookup and this waste time so for this case the time complexity is O(n*k), when doing sliding window we create a window sum and each one loop we are adding next element in the sum and removing the 1st element from the sum we arent doing like making the sum from scratch just moving the window to get the next window sum so for this case we have only one lookup using for loop so it is O(n) complexity.

## Q2 (trace)

**Trace `max_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], k=3)`. Write the window sum after each slide, then give the final answer.**

```python
def max_sum(nums, k):
    window = sum(nums[:k])
    best = window

    for right in range(k, len(nums)):
        window += nums[right]
        window -= nums[right - k]
        best = max(best, window)

    return best


max_sum([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], k=3)
```

```text
1st window: [4, 2, 1], 7, 8, 1, 2, 8, 1, 0 -> sum = 7 -> best = 7
2nd window: right = 3, nums[3] = 7, nums[0] = 4 -> 4, [2, 1, 7], 8, 1, 2, 8, 1, 0 -> sum = 10 -> best = 10
3rd window: right = 4, nums[4] = 8, nums[1] = 2 -> 4, 2, [1, 7, 8], 1, 2, 8, 1, 0 -> sum = 16 -> best = 16
4th window: right = 5, nums[5] = 1, nums[2] = 1 -> 4, 2, 1, [7, 8, 1], 2, 8, 1, 0 -> sum = 16 -> best = 16
5th window: right = 6, nums[6] = 2, nums[3] = 7 -> 4, 2, 1, 7, [8, 1, 2], 8, 1, 0 -> sum = 11 -> best = 16
6th window: right = 7, nums[7] = 8, nums[4] = 8 -> 4, 2, 1, 7, 8, [1, 2, 8], 1, 0 -> sum = 11 -> best = 16
7th window: right = 8, nums[8] = 1, nums[5] = 1 -> 4, 2, 1, 7, 8, 1, [2, 8, 1], 0 -> sum = 11 -> best = 16
8th window: right = 9, nums[9] = 0, nums[6] = 2 -> 4, 2, 1, 7, 8, 1, 2, [8, 1, 0] -> sum = 9 -> best = 16

best = 16
```

## Q3

**In the code, why is the element leaving `nums[right - k]` and not `nums[right - k + 1]`?**

when right = k our first adding element is nums[k] which is exactly next element of the window for example if k = 3 so the first adding element will be 4th element and when we do nums[right - k] for the leaving element we get 3 - 3 = 0 which is the 1st element of the array, which we exactly want for 3 element window tracing remove the 1st element and add the 4th element in our first loop.

## Q4

**Which of these can use a fixed-size sliding window? Say yes or no for each, with a short reason.**

- a) Average of every 5 consecutive days of temperatures
- b) Longest subarray whose sum is ≤ 10
- c) Maximum number of vowels in any substring of length k

a) Average of every 5 consecutive days of temperatures -> yes -> because you fixed with the number 5 it means i can only look for 5 consecutive days there is no extend or shrink in the window of days.

b) Longest subarray whose sum is ≤ 10 -> no -> when solving this problem we need to extend the window to find the longest one.

c) Maximum number of vowels in any substring of length k -> yes -> we are looking for the max number of vowels in a fixed length of substring. if string is like "owjefamslfjw" and the substring length is 4 the window will be like [owje] next window will be like [wjef] and from there we need to find the max vowels.

## Q5 (code)

**Write `max_average(nums, k)`, which returns the maximum average of any subarray of length k. (This is LeetCode 643.)**

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / k
```

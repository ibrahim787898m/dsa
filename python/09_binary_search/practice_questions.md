# Binary Search — Practice Questions

## Quiz questions from the session

Redo these without notes. The ones marked **(redo)** are the ones you missed or only got partly right the first time. For code questions, run them and check the output.

### Quiz 1: The idea

1. Array `[3, 9, 14, 20, 27, 31, 40, 48]`, target 31. Write each step: range, mid, value, decision. Use `mid = (low + high) // 2`.
2. Why might binary search fail on `[7, 2, 9, 4, 1]` when looking for 4? What would you have to do first, and what would it cost in Big O?
3. **(redo)** An array has about 1,000,000,000 elements. Roughly how many comparisons does binary search need in the worst case? Explain how you got it.
4. Roughly how many comparisons for 1,000,000,000,000 (1 trillion) elements?

### Quiz 2: The code

1. **(redo)** Trace `[2, 5, 8, 11, 15, 19, 24]`, target 20. Write low, high, mid, value and action at each step, including the final pointer update. What does it return, and what is `low` when it stops?
2. Find the bug. Which line causes an infinite loop, and what input triggers it?

   ```python
   def search(nums, target):
       low, high = 0, len(nums) - 1
       while low <= high:
           mid = (low + high) // 2
           if nums[mid] == target:
               return mid
           elif nums[mid] < target:
               low = mid
           else:
               high = mid - 1
       return -1
   ```

3. Write `binary_search(nums, target)` from memory. Test it with `[1, 3, 5, 7]` and targets 1, 7 and 4.

### Quiz 3: Variants

1. Trace **last occurrence** on `[2, 4, 4, 4, 4, 7]`, target 4. Include `result` at each step.
2. **(redo)** Write `count(nums, target)` in O(log n) using first and last occurrence. What should it return if the target isn't in the array? Test with a missing target and an empty array.
3. What does `search_insert([1, 3, 5, 6], target)` return for targets 0, 7 and 4? Explain the results for 0 and 7.

### Quiz 4: Advanced patterns

1. **(redo)** Trace `search_rotated` on `[6, 7, 8, 1, 2, 3, 4, 5]`, target 2. At each step write low, high, mid, value, **which half is sorted** (compare with `nums[low]`), and the decision.
2. Write `my_sqrt(x)` from memory. Test with x = 0, 1, 8, 16 (expected 0, 1, 2, 4).
3. **(redo)** Koko Eating Bananas with `piles = [3, 6, 7, 11]`, `h = 8`: what are `low` and `high` for the speed range, and why? What does `can_finish(k)` compute?

## Extra practice questions

New questions, from easier to harder. Do the traces by hand first, then run the code to confirm.

### Tracing

1. Trace the standard template on `[1, 4, 7, 10, 13, 16, 19, 22, 25]`, target 25. How many comparisons did it take? Is that the worst case for 9 elements?
2. Trace **first occurrence** of 5 in `[1, 5, 5, 5, 5, 5, 9]`. Show `result` at every step.
3. What does `search_insert([2, 4, 6, 8, 10], target)` return for targets 5, 11 and 1? Trace the target 5 case.
4. Trace `search_rotated` on `[4, 5, 6, 7, 0, 1, 2]` for target 0, then for target 3 (not in the array). Name the sorted half at each step.

### Bugs and reasoning

1. Someone writes the standard template with `while low < high` instead of `<=`. Give the smallest input where it returns the wrong answer, and explain why.
2. You need to search the same unsorted array of n items m times. Compare the total cost of (a) linear search every time and (b) sorting once, then binary searching every time. Roughly when does (b) win?
3. Your array is sorted in **descending** order, like `[9, 7, 5, 3, 1]`. Which two lines of the standard template change? Write the descending version and test it with targets 3, 9 and 4.

### Writing code (run and paste the output)

1. Write `last_occurrence(nums, target)` from memory. Test it on `[1, 2, 2, 2, 3]` with target 2, plus a missing target and an empty array.
2. Write `cube_root(x)` that returns the largest integer `k` with `k * k * k <= x`. Test with x = 0, 1, 7, 8, 27, 100.
3. A sorted m × n matrix (each row sorted, and each row's first value is bigger than the last value of the row above) can be searched as one long sorted array of length m × n. Given a 1D index `i`, what are its row and column? Write the search. This is LeetCode 74.

### Binary search on the answer (setup only, then code)

1. Ship packages: weights `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` must ship in order within 5 days. Each day the ship carries a contiguous group up to its capacity. What are `low` and `high` for the capacity, and why? Describe `can_ship(capacity)` in words. This is LeetCode 1011.
2. Finish Koko Eating Bananas in code: write `can_finish(k)` first and test it on the table in the concept notes (speeds 3, 4, 5, 11), then add the binary search around it.

## LeetCode problems

All 15 are unsolved so far. Work through them in order: the first 6 are the ones from the lessons, then extra problems grouped by pattern. Update the Status column as you go.

| # | Problem | Difficulty | Pattern | Status |
| --- | --- | --- | --- | --- |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Standard template | Not started |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Insert position (return low) | Not started |
| 34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | First + last occurrence | Not started |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Rotated array | Not started |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | Search on answer (last valid) | Not started |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Search on answer (first valid) | Not started |
| 374 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | Easy | Standard template | Not started |
| 278 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | First occurrence (first true) | Not started |
| 367 | [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | Easy | Search on answer | Not started |
| 744 | [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | Easy | Insert position variant | Not started |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Standard template on index math | Not started |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Rotated array | Not started |
| 852 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | Medium | Compare mid with neighbour | Not started |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | Compare mid with neighbour | Not started |
| 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Search on answer (first valid) | Not started |

Tip: before coding each one, write down which template from the concept notes it uses and the edge cases you'll test.

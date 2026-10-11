# Binary Search — Quiz 4 (the last one)

## Q1 (trace)

**Run `search_rotated` on [6, 7, 8, 1, 2, 3, 4, 5] with target 2. At each step, write low, high, mid, the value, which half is sorted, and your decision.**

```text
step 1 -> low 0 -> high 7 -> mid 3 -> value 1 -> 1 < 6 -> 1 < target 2 <= 5 matches -> low 4
step 2 -> low 4 -> high 7 -> mid 5 -> value 3 -> 3 < 6 -> 3 < target 2 <= 5 not match -> high 4
step 3 -> low 4 -> high 4 -> mid 4 -> value 2 -> return 4
```

## Q2 (write and run it)

**Write `my_sqrt(x)` from memory, run it in Vim, and paste it. Test it with x = 0, 1, 8, 16. (Expected: 0, 1, 2, 4.)**

```python
def my_sqrt(x):
    low, high = 0, x
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= x:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res
```

## Q3 (think it through)

**For Koko Eating Bananas with piles = [3, 6, 7, 11] and h = 8:**

- What should low and high be for the speed range, and why?
- In words, what does the check `can_finish(k)` do?

low 1 because in question it says koko likes to eat slow so the slowest one is 1 banana per hour. high might be 11 here because in this case h can be 4 the lowest according to the condition piles.length <= h <= 10^9, h = 4 if it is, koko needs to eat 11 banana per hour cause there are only 4 piles and in one pile number of banana is 11, if koko doesnot eat 11 banana per hour koko cant finish it.

can_finish(k) i guess it does check if koko can finish k number of banana from each pile before coming the guard.

# Binary Search — Quiz 3

## Q1 (trace)

**Run last occurrence on [2, 4, 4, 4, 4, 7] with target 4. Write out each step, including result.**

```text
step 1 -> low 0 -> high 5 -> mid 2 -> value 4 -> match go right -> result 2
step 2 -> low 3 -> high 5 -> mid 4 -> value 4 -> match go right -> result 4
step 3 -> low 5 -> high 5 -> mid 5 -> value 7 -> 7 > 4 -> low 5 high 4 -> loops end
result = 4
```

## Q2 (count it)

**Using first and last occurrence, write a function `count(nums, target)` that returns how many times target appears, in O(log n). What should it return if the target isn't in the array?**

```python
def count_occurrence(nums, target):

    def first_occurrence(l, h):
        res = -1
        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                res = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return res

    def last_occurrence(l, h):
        res = -1
        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                res = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return res

    low, high = 0, len(nums) - 1

    if first_occurrence(low, high) == -1:
        return 0

    return last_occurrence(low, high) - first_occurrence(low, high) + 1


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(count_occurrence(nums, target))
```

## Q3 (predict it)

**What does `search_insert([1, 3, 5, 6], target)` return for target 0, then 7, then 4? Explain why 0 and 7 give the answers they do.**

```text
target 0 → 0
target 7 → 4
target 4 → 2
```

for 0, 0 is smaller value of all of the values so when target is smaller than the all values we always check left and discard right so low always stays at 0th index and thats why we get the this answer

for 7, 7 is bigger value of all of the values so when target is bigger than the all values we always check right and discard left so right stays at the last most index so when the low become greater than the high the loops and and does not found the target and this low is the index when we insert the value 7

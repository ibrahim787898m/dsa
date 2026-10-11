# Binary Search — Quiz 2

## Q1 (trace)

**nums = [2, 5, 8, 11, 15, 19, 24], target = 20. Write out each step with low, high, mid, value and action. What does it return, and what is low when it stops?**

```text
step 1 -> low 0 -> high 6 -> mid 3 -> value 11 -> 11 < 20 -> discard left
step 2 -> low 4 -> high 6 -> mid 5 -> value 19 -> 19 < 20 -> discard left
step 3 -> low 6 -> high 6 -> mid 6 -> value 24 -> 26 > 20 -> loop ends
-> not found -> return -1
```

## Q2 (find the bug)

**This code sometimes runs forever. Find the line that causes it and give an input that triggers the infinite loop.**

```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid #this line is bug. when we dont increase the index by one if nums length is odd 7, at a point in the end it will repeat the low = 5 and high = 6 and wont end. for example nums = [2, 5, 8, 11, 15, 19, 24], target = 20 -> 0:6 - 3:6 - 4:6 - 5:6 - 5:6 ......
        else:
            high = mid - 1
    return -1
```

## Q3 (write it)

**Without looking at the template, write `binary_search(nums, target)` from memory. Then test it with [1, 3, 5, 7] for each of these targets: 1, 7, 4. (Run it in Python if you can.)**

```python
def search(nums, target):
    low, high = 0, len(nums - 1)

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

```text
target 1 -> mid 0
target 7 -> mid 3
target 4 -> return -1
```

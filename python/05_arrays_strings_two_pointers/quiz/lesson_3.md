# Two Pointers — Quiz: Lesson 3

## Q1

**In Two Sum II, when total > target we move right left. Why can we safely skip every pair that uses the current right, without checking them? (Explain in words.)**

in two sum ii problem as it is sorted that means the large values are iin the right and small values in the left so if i found that total is getting bigger than the target that means all right side element will make the total bigger so we can skip these and work with the left side elements

## Q2

**Which pattern would you use for each of these? Give just the pattern name and a one-line reason.**

- (a) Reverse a list in place
- (b) Check whether two sorted lists have any element in common
- (c) Remove all occurrences of val from a list in place

a. we will use two pointer from both end towards inward. like we will replace left most and the right most element first then move inward and do this again until left is less than right.

b. so there is 2 different array so we will use 2 different pointer starting from same index so x = y = 0 and check each index for both array to find the common element.

c. here we will use two pointer for same array from same direction one will move slow and another will move fast and compare with the slow one to find the occurrences if we dont find the occurrence we will move slow by one and replace the previous same value with the unique value.

## Q3

**Write `move_zeroes(nums)`, which moves all 0s to the end in place and keeps the order of the other numbers.**

```text
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
[0]              → [0]
[1, 2]           → [1, 2]
```

```text
def move_zeroes(nums):
    if not nums: O(1)
        return 0 O(1)

    i = 0 O(1)
    for j in range(1, len(nums)): O(1) * n times
        if nums[j] != 0: O(1)
            nums[i], nums[j] = nums[j], nums[i] O(1)
            i += 1 O(1)
    return nums O(1)
```

time complexity: (O(1) * O(1)) + O(1) + (n * O(1) * O(1)  * O(1) + O(1)) + O(1) = O(n)

space complexity: O(1) because in place

## Q4 (thinking question)

**Why does Two Sum II's two-pointer trick fail on an unsorted array?**

because when we will match the total with the target will will get the two index number and add by 1 because for this case it start from 1st index but in general two pointer problem index start from 0 so we will get wrong index if we use two pointer of ii version in the origial one
